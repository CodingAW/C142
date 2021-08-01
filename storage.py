import csv

all_movies = []

with open('final.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

