#!/usr/bin/python
import csv

database = []
year_grouped= {}

with open("database/rounds.csv") as file:
    reader = csv.reader(file)
    prev = ""
    for row in reader:
        entry = {
            "year": row[0],
            "day": row[1],
            "time": row[2],
            "type": row[3],
            "number": row[4],
            "name": row[5],
            "duration": row[6],
            "points": row[7]
        }
        database.append(entry)
        if entry["year"] not in year_grouped:
            year_grouped[entry["year"]] = []
        year_grouped[entry["year"]].append(entry)
