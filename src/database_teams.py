#!/usr/bin/python
import csv
from database_countries import code_to_country as c_t_c

database = []
code_grouped = {}
year_grouped = {}

with open("database/teams.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        entry = {
            "year": row[0],
            "rank": row[1],
            "code": row[2],
            "tier": row[3],
            "official_rank": row[4],
            "total_score": row[5],
            "team_total": row[6],
            "team_1": row[7],
            "team_2": row[8],
            "team_3": row[9],
            "team_4": row[10],
            "team_5": row[11],
            "team_6": row[12],
            "individual_total": row[13],
            "individual_1": row[14],
            "individual_2": row[15],
            "individual_3": row[16],
            "individual_4": row[17],
            "individual_5": row[18],
            "individual_6": row[19],
            "individual_7": row[20],
            "individual_8": row[21],
            "individual_9": row[22],
            "individual_10": row[23],
            "individual_11": row[24],
            "individual_12": row[25],
            "individual_13": row[26],
            "individual_14": row[27],
            "individual_15": row[28],
            "individual_16": row[29],
            "individual_17": row[30],
        }
        if (entry["code"] != "???") and (entry["code"] not in c_t_c):
            raise Exception("Team database corrupted! Row: {}".format(row))
        database.append(entry)
        if entry["code"] not in code_grouped:
            code_grouped[entry["code"]] = []
        code_grouped[entry["code"]].append(entry)
        if entry["year"] not in year_grouped:
            year_grouped[entry["year"]] = []
        year_grouped[entry["year"]].append(entry)
