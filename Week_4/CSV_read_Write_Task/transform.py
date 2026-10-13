import csv


## The task is to transform the IMDB data using the below criteria:

#only the films from 2010 onwards should be selected
#movies should be the only title type
#only the primary title should be used
#remove the end date and isadult fields entirely


new_lines = []

with open("imdbtitles.csv") as csvfile:
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

with open("imdb_movies_2010_plus.csv", "w", newline="") as output:
    csv.writer(output).writerows(new_lines)

print(len(new_lines) - 1, "movies kept")