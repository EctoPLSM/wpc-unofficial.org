#!/usr/bin/python
import csv
from database_countries import code_to_country as c_t_c

database = []
code_grouped = {}
year_grouped = {}

with open("database/participants.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        entry = {
            "year": row[0],
            "rank": row[1],
            "name": row[2],
            "code": row[3],
            "tier": row[4],
            "official_rank": row[5],
            "under_18": row[6],
            "over_50": row[7],
            "rookie": row[8],
            "total_score": row[9],
            "individual_1": row[10],
            "individual_2": row[11],
            "individual_3": row[12],
            "individual_4": row[13],
            "individual_5": row[14],
            "individual_6": row[15],
            "individual_7": row[16],
            "individual_8": row[17],
            "individual_9": row[18],
            "individual_10": row[19],
            "individual_11": row[20],
            "individual_12": row[21],
            "individual_13": row[22],
            "individual_14": row[23],
            "individual_15": row[24],
            "individual_16": row[25],
            "individual_17": row[26],
        }
        if entry["code"] != "???" and entry["code"] not in c_t_c:
            raise Exception("Competitor database corrupted! Row: {}".format(row))
        database.append(entry)
        if entry["code"] not in code_grouped:
            code_grouped[entry["code"]] = []
        code_grouped[entry["code"]].append(entry)
        if entry["year"] not in year_grouped:
            year_grouped[entry["year"]] = []
        year_grouped[entry["year"]].append(entry)
