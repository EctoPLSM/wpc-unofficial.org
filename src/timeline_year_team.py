#!/usr/bin/python
import itertools
import sys
import util
import templates
from database_countries import code_to_country
from database_participants import year_grouped as p_db_y
from database_timeline import year_indexed as t_db_y
from database_timeline import previous_year
from database_timeline import next_year
from database_teams import year_grouped as team_db_y
from database_rounds import year_grouped as r_db_y
from functools import cmp_to_key

def run(year):
    print("Creating timeline/" + year + "/team")
    html = templates.get("timeline/year/team")
    html = templates.initial_replace(html, 1)
    yeardata = t_db_y[year]
    html = html.replace("__YEAR__", year)
    html = html.replace("__NUMBER__", yeardata["number"])
    html = html.replace("__ORDINAL__", util.ordinal(yeardata["number"]))
    
    if year in previous_year:
        html = html.replace("__PREVIOUS_YEAR__", previous_year[year])
        html = html.replace("__PREVIOUS_YEAR_STYLE__", "")
    else:
        html = html.replace("__PREVIOUS_YEAR_STYLE__", "display: none;")
        html = html.replace("__PREVIOUS_YEAR__", ".") # Google crawler fix
        
    if year in next_year:
        html = html.replace("__NEXT_YEAR__", next_year[year])
        html = html.replace("__NEXT_YEAR_STYLE__", "")
    else:
        html = html.replace("__NEXT_YEAR_STYLE__", "display: none;")
        html = html.replace("__NEXT_YEAR__", ".") # Google crawler fix
    
    individual_rounds = 0
    team_rounds = 0
    individual_column = "<th data-sortinitialorder=\"desc\">Total</th>\n"
    team_column = "<th data-sortinitialorder=\"desc\">Total</th>\n"
    tablehtml = ""
    prevcode = ""
    prevrank = 0

    if year in team_db_y:
        if int(year) >= 1999:
            for row in r_db_y[year]:
                if row["points"] != "#":
                    if row["type"] == "Individual":
                       individual_rounds += 1
                    else:
                        team_rounds += 1
            team_column += ""
            for row in r_db_y[year]:
                if row["points"] != "#":
                    if row["type"] == "Individual":
                        individual_column += "<th data-sortinitialorder=\"desc\">" + row["number"].split(" ")[-1] + "</th>\n"
                    else:
                        team_column += "<th data-sortinitialorder=\"desc\">" + row["number"].split(" ")[-1] + "</th>\n"
        html = html.replace("__TEAM__", "<th class=\"sorter-false\" colspan=\"" +  str(team_rounds+1) + "\">Team Rounds</th>\n")
        html = html.replace("__INDIVIDUAL__", "<th class=\"sorter-false\" colspan=\"" +  str(individual_rounds+1) + "\">Individual Rounds</th>\n")
        html = html.replace("__TEAM_DETAILS__", team_column)
        html = html.replace("__INDIVIDUAL_DETAILS__", individual_column)
        
        for row in team_db_y[year]:
            rowhtml = templates.get("timeline/year/team_row")
            rowhtml = rowhtml.replace("__CODE__", row["code"])
            if row["code"] != "???":
                rowhtml = rowhtml.replace("__COUNTRY__", code_to_country[row["code"]])
            else:
                rowhtml = rowhtml.replace("__COUNTRY__", "???")
            rowhtml = rowhtml.replace("__TIER__", row["tier"])
            rowhtml = rowhtml.replace("__RANK__", row["rank"])
            rowhtml = rowhtml.replace("__OFFICIAL_RANK__", row["official_rank"])
            rowhtml = rowhtml.replace("__TOTAL_SCORE__", row["total_score"])

            team_rounds_row = ""
            for i in range(0, team_rounds+1):
                if i == 0:
                    team_rounds_row += "<td align=\"right\">" + row["team_total"] + "</td>\n"
                else:
                    team_rounds_row += "<td align=\"right\">" + row["team_" + str(i)] + "</td>\n"
            rowhtml = rowhtml.replace("__TEAM_ROUNDS__", team_rounds_row)

            individual_rounds_row = ""
            for i in range(0, individual_rounds+1):
                if i == 0:
                    individual_rounds_row += "<td align=\"right\">" + row["individual_total"] + "</td>\n"
                else:
                    individual_rounds_row += "<td align=\"right\">" + row["individual_" + str(i)] + "</td>\n"
            rowhtml = rowhtml.replace("__INDIVIDUAL_ROUNDS__", individual_rounds_row)
            tablehtml += rowhtml
    html = html.replace("__TABLE__", tablehtml)
    
    html = templates.final_replace(html, "../..")
    util.writefile("../timeline/" + year + "/team.html", html)
    
if __name__ == "__main__":
    run(sys.argv[1])
