# Reading and Writing Files and CSVs in Python

## 1. Opening files

```python
open(filename, mode)
```

| Mode | Meaning |
|---|---|
| `"r"` | Read (default). Error if the file doesn't exist |
| `"w"` | Write. **Erases** existing content |
| `"a"` | Append. Adds to the end |
| `"x"` | Create new. Error if the file already exists |
| `"+"` | Add reading and writing (`r+`, `w+`, `a+`) |
| `"b"` / `"t"` | Binary / text (text is the default) |

Always use `with`, which closes the file automatically, even if an error occurs:

```python
with open("order.txt", "r") as f:
    ...
```

---

## 2. Reading a text file

```python
with open("order.txt", "r") as f:
    for line in f:              # one line per pass
        print(line.strip())     # strip() removes the hidden \n
```

| Method | Returns |
|---|---|
| `f.read()` | The whole file as one string |
| `f.readline()` | One line |
| `f.readlines()` | A list of all lines |

The file is read **once**. After reading, the pointer is at the end (use `f.seek(0)` to go back).

---

## 3. Writing to a text file

```python
def write_to_file(file, order_item):
    with open(file, "a") as f:
        f.write(order_item + "\n")
```

- `write()` only accepts **strings**. Convert numbers with `str()`.
- `write()` does **not** add a newline. Use `"\n"` (backslash, not `/n`).
- Use `"a"` to add to a file. `"w"` wipes it every time.
- It returns the number of characters written.

---

## 4. Closing files and `try/finally`

If an error happens before `close()`, the file stays open. Two fixes:

```python
# try/finally: finally always runs
f = open("order.txt", "r")
try:
    data = f.read()
finally:
    f.close()

# with: does the same thing automatically (preferred)
with open("order.txt", "r") as f:
    data = f.read()
```

---

## 5. Handling errors

```python
try:
    with open("order.txt", "x") as f:
        f.write("Burger\n")
except FileExistsError:
    print("order.txt already exists")
except FileNotFoundError:
    print("File not found")
```

- `except` must name the **same error** that is raised (read the last line of the traceback).
- The risky code must be **inside** the `try` block.
- Put specific exceptions before general ones.

| Error | Cause |
|---|---|
| `FileNotFoundError` | Opening a missing file in `"r"` mode, or a wrong path |
| `FileExistsError` | Opening an existing file in `"x"` mode |
| `ValueError` | e.g. `int("\N")` |
| `IndexError` | A row shorter than expected (e.g. a blank line) |

---

## 6. CSV files

CSV (comma-separated values) is a plain-text table. Each line is a row and commas separate the columns.

```
name,position,salary
Jude,Midfielder,520000
```

**Why use CSV:** simple, universal (Excel, databases, Python), small, human-readable.
**Limits:** everything is text (convert with `int()`), flat structure only, no formatting.

### Reading

```python
import csv

with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)          # takes the header row out
    for row in reader:             # each row is a list of strings
        print(row[0], row[2])
```

### Writing

```python
with open("out.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "salary"])        # one row
    writer.writerows([["Jude", 520000],        # many rows
                      ["Harry", 2600000]])
```

- Keep `newline=""` to avoid blank lines between rows on Windows.
- Use the **same encoding** (`utf-8`) for reading and writing.
- Quoted values containing commas (e.g. `"Comedy,Drama"`) are handled for you.

### List of lists vs flat list

```python
[["Jude", "Midfielder"], ["Harry", "Striker"]]   # list of lists: rows stay together
["Jude", "Midfielder", "Harry", "Striker"]       # flat list: structure is lost
```

A list of lists keeps each record together: `data[1][0]` is row 1, column 0.

`csv.DictReader` gives each row as a dictionary, so you use column names instead of index numbers:

```python
with open("data.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["salary"])
```

---

## 7. Worked example: transforming the IMDB data

**Task:** keep only movies from 2010 onwards, use only the primary title, and remove `endYear` and `isAdult`.

| Index | Column | Action |
|---|---|---|
| 0 | titleType | Filter (`"movie"`) and keep |
| 1 | primaryTitle | Keep |
| 2 | originalTitle | Drop |
| 3 | isAdult | Drop |
| 4 | startYear | Filter (>= 2010) and keep |
| 5 | endYear | Drop |
| 6 | runtimeMinutes | Keep |
| 7 | genres | Keep |

```python
import csv

new_lines = []                                    # created once, before the loop

with open("imdbtitles.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    new_lines.append([header[0], header[1], header[4], header[6], header[7]])

    for lines in reader:
        try:
            year = int(lines[4])
        except ValueError:                        # "\N" = missing value
            continue

        if lines[0] == "movie" and year >= 2010:
            new_lines.append([lines[0], lines[1], lines[4], lines[6], lines[7]])

with open("imdb_movies_2010_plus.csv", "w", newline="", encoding="utf-8") as output:
    csv.writer(output).writerows(new_lines)

print(len(new_lines) - 1, "movies kept")          # minus 1 for the header
```

### As a function

```python
def transform_imdb(input_file, output_file):
    new_lines = []
    with open(input_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        new_lines.append([header[0], header[1], header[4], header[6], header[7]])
        for lines in reader:
            try:
                year = int(lines[4])
            except ValueError:
                continue
            if lines[0] == "movie" and year >= 2010:
                new_lines.append([lines[0], lines[1], lines[4], lines[6], lines[7]])

    with open(output_file, "w", newline="", encoding="utf-8") as output:
        csv.writer(output).writerows(new_lines)

    return len(new_lines) - 1
```

Parameters replace the hard-coded file names, and returning the count (instead of printing) makes it easy to test.

---

## 8. Common mistakes

| Mistake | Fix |
|---|---|
| `new_list = []` inside the loop, so only the last row survives | Create the list **before** the loop |
| `"/n"` instead of `"\n"` | Newline is a **backslash** |
| Using `"w"` when you meant to add to a file | Use `"a"` |
| `IndexError: list index out of range` | A blank or short row. Check `len(row)` first |
| `int("\N")` crashes | Wrap in `try/except ValueError` |
| `except` never triggers | Wrong exception type, or code is outside the `try` |
| Comparing a CSV year to a number without `int()` | CSV values are always strings |
| Output overwrites the input file | Use a different output file name |
| Garbled characters (e.g. `âˆš`) | Encoding mismatch. Use `encoding="utf-8"` and check the source file |
| `FileNotFoundError` | The file isn't in the folder you run from, so check the path |

---

## 9. Quick reference

```python
# Read lines            # Write a line          # Read CSV            # Write CSV
for line in f:          f.write(text + "\n")    csv.reader(f)         csv.writer(f)
    line.strip()                                next(reader)          writer.writerows(rows)
```