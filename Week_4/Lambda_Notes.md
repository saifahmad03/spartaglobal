# Lambda Functions in Python

## What is a lambda?

A **lambda** is a small, anonymous function written in a single line. "Anonymous" means it doesn't need a name (though you can give it one by assigning it to a variable).

**Syntax:**

```python
lambda arguments: expression
```

- `lambda` is the keyword.
- `arguments` are the inputs, just like in a normal function (zero or more, separated by commas).
- `expression` is a single expression whose result is automatically **returned**. There is no `return` keyword.

---

## Lambda vs a normal function

These two do exactly the same thing:

```python
# Normal function
def add(a, b):
    return a + b

# Lambda equivalent
add = lambda a, b: a + b

print(add(2, 3))  # 5
```

The lambda version is shorter, but not necessarily better. Lambdas shine when you need a **quick, throwaway function** that you'll use once, usually as an argument to another function.

---

## Basic examples

### One argument

```python
square = lambda x: x ** 2
print(square(5))  # 25
```

### Multiple arguments

```python
multiply = lambda a, b: a * b
print(multiply(4, 6))  # 24
```

### No arguments

```python
greet = lambda: "Hello, world!"
print(greet())  # Hello, world!
```

### Default arguments

```python
power = lambda base, exp=2: base ** exp
print(power(3))     # 9  (uses default exp=2)
print(power(3, 3))  # 27
```

### Calling immediately

You can define and call a lambda in one go (rarely useful, but it shows what's happening):

```python
print((lambda x, y: x + y)(10, 5))  # 15
```

---

## Conditional logic inside a lambda

A lambda can only contain an *expression*, not statements like `if ... :` blocks. But you can use the **ternary (conditional) expression**:

```python
# value_if_true if condition else value_if_false
is_even = lambda n: "even" if n % 2 == 0 else "odd"

print(is_even(4))  # even
print(is_even(7))  # odd
```

```python
# Find the larger of two numbers
bigger = lambda a, b: a if a > b else b
print(bigger(10, 20))  # 20
```

---

## Where lambdas are really useful

The most common use is passing a small function into another function. Here are the big four.

### 1. `sorted()` and `.sort()` with a `key`

The `key` tells Python *what to sort by*.

```python
words = ["banana", "kiwi", "apple", "cherry"]

# Sort by length
print(sorted(words, key=lambda w: len(w)))
# ['kiwi', 'apple', 'banana', 'cherry']
```

Sorting a list of tuples by the second item:

```python
students = [("Alice", 88), ("Bob", 95), ("Cara", 72)]

by_score = sorted(students, key=lambda s: s[1])
print(by_score)
# [('Cara', 72), ('Alice', 88), ('Bob', 95)]

# Highest score first
by_score_desc = sorted(students, key=lambda s: s[1], reverse=True)
print(by_score_desc)
# [('Bob', 95), ('Alice', 88), ('Cara', 72)]
```

Sorting a list of dictionaries:

```python
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Cara", "age": 35},
]

print(sorted(people, key=lambda p: p["age"]))
# [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Cara', 'age': 35}]
```

### 2. `map()`: transform every item

`map(function, iterable)` applies the function to each item.

```python
numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]
```

```python
names = ["alice", "bob", "cara"]
print(list(map(lambda n: n.title(), names)))
# ['Alice', 'Bob', 'Cara']
```

> `map()` returns an iterator, so wrap it in `list()` to see the results.

### 3. `filter()`: keep only items that pass a test

`filter(function, iterable)` keeps items where the function returns `True`.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8]
```

```python
words = ["hi", "hello", "hey", "greetings"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)  # ['hello', 'greetings']
```

### 4. `reduce()`: combine everything into one value

`reduce` lives in `functools`. It repeatedly applies a two-argument function to accumulate a result.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda acc, x: acc + x, numbers)
print(total)  # 15

product = reduce(lambda acc, x: acc * x, numbers)
print(product)  # 120
```

How the sum works step by step:

```
acc=1, x=2 -> 3
acc=3, x=3 -> 6
acc=6, x=4 -> 10
acc=10, x=5 -> 15
```

---

## Other handy places to use lambdas

### `min()` and `max()` with a `key`

```python
products = [("pen", 1.50), ("book", 12.99), ("bag", 25.00)]

cheapest = min(products, key=lambda p: p[1])
priciest = max(products, key=lambda p: p[1])

print(cheapest)  # ('pen', 1.5)
print(priciest)  # ('bag', 25.0)
```

### Storing lambdas in a dictionary

A neat way to build a simple "calculator":

```python
operations = {
    "add":      lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide":   lambda a, b: a / b,
}

print(operations["add"](10, 5))       # 15
print(operations["multiply"](10, 5))  # 50
```

### Functions that return functions

```python
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))  # 20
print(triple(10))  # 30
```

This works because the lambda "remembers" the value of `n` (this is called a *closure*).

### Callbacks (e.g. in GUI or event code)

```python
buttons = []
for label in ["Save", "Open", "Exit"]:
    buttons.append(lambda l=label: print(f"{l} clicked"))

buttons[0]()  # Save clicked
buttons[2]()  # Exit clicked
```

(The `l=label` default argument is important; see the pitfalls section below.)

---

## Lambda limitations

1. **Only one expression.** No multiple statements, no `if/for/while` blocks, no assignments (`x = 5`), no `return`.
2. **Harder to debug.** Tracebacks show `<lambda>` instead of a helpful function name.
3. **No docstrings or type annotations** on the lambda itself.
4. **Readability drops fast** when a lambda gets complicated.

If your logic needs more than a simple expression, use a regular `def`.

---

## Common pitfalls

### Pitfall 1: Late binding in loops

```python
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])  # [2, 2, 2]  <- surprising!
```

All the lambdas look up `i` when they are *called*, by which time the loop has finished and `i == 2`. Fix it by capturing the value with a default argument:

```python
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2]
```

### Pitfall 2: Assigning a lambda to a name

PEP 8 (Python's style guide) discourages this:

```python
# Discouraged
square = lambda x: x ** 2

# Preferred
def square(x):
    return x ** 2
```

If you're giving it a name anyway, a `def` is clearer and gives better error messages. Save lambdas for inline, throwaway use.

### Pitfall 3: Overcomplicating

```python
# Hard to read
result = list(map(lambda x: x * 2 if x % 2 == 0 else x * 3, filter(lambda x: x > 0, data)))

# Clearer: a list comprehension
result = [x * 2 if x % 2 == 0 else x * 3 for x in data if x > 0]
```

For simple transformations and filters, list comprehensions are often more readable than `map`/`filter` with lambdas.

---

## When should you use a lambda?

**Good uses**

- A short `key=` function for `sorted`, `min`, `max`
- A quick one-off function passed to `map`, `filter`, or `reduce`
- Small callbacks
- Tiny functions in a dictionary of operations

**Better to use `def`**

- The logic is more than one simple expression
- You'll reuse the function in several places
- You want a docstring, type hints, or a clear name in error messages

---

## Quick cheat sheet

| Goal | Example |
|------|---------|
| Basic lambda | `lambda x: x + 1` |
| Multiple args | `lambda a, b: a * b` |
| Conditional | `lambda x: "yes" if x > 0 else "no"` |
| Sort by key | `sorted(items, key=lambda i: i[1])` |
| Transform | `list(map(lambda x: x * 2, nums))` |
| Filter | `list(filter(lambda x: x > 0, nums))` |
| Reduce | `reduce(lambda a, b: a + b, nums)` |
| Max by key | `max(items, key=lambda i: i["score"])` |

---

## Summary

- A lambda is a **small anonymous function**: `lambda args: expression`.
- It automatically returns the value of its single expression.
- It's most useful as a short function passed to `sorted`, `map`, `filter`, `reduce`, `min`, and `max`.
- Keep lambdas **simple**. When in doubt, write a normal function.