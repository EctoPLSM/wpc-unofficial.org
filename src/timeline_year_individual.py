#!/usr/bin/python
import sys
import util
import templates
from database_countries import code_to_country
from database_participants import year_grouped as p_db_y
from database_timeline import year_indexed as t_db_y
from database_timeline import previous_year
from database_timeline import next_year
from database_rounds import year_grouped as r_db_y
from database_teams import year_grouped as team_db_y

def run(year):
    print("Creating timeline/" + year + "/individual")
    html = templates.get("timeline/year/individual")
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
    individual_column = "<th data-sortinitialorder=\"desc\">Total</th>\n"
    tablehtml = ""
    prevcode = ""
    prevrank = 0

    if year in r_db_y:
        for row in r_db_y[year]:
            if row["type"] == "Individual" and row["points"] != "#":
               individual_rounds += 1
               individual_column += "<th data-sortinitialorder=\"desc\">" + row["number"].split(" ")[-1] + "</th>\n"
        html = html.replace("__INDIVIDUAL_DETAILS__", individual_column)
    
    if int(year) >= 2013:
        html = html.replace("__SPECIAL__", "<th>U18</th>\n<th>O50</th>")
    else:
        html = html.replace("__SPECIAL__", "")
    if year in p_db_y:
        for row in p_db_y[year]:
            rowhtml = templates.get("timeline/year/individual_row")
            rowhtml = rowhtml.replace("__NAME__", row["name"])
            rowhtml = rowhtml.replace("__CODE__", row["code"])
            if row["code"] != "???":
                rowhtml = rowhtml.replace("__COUNTRY__", code_to_country[row["code"]])
            else:
                rowhtml = rowhtml.replace("__COUNTRY__", "???")
            rowhtml = rowhtml.replace("__TIER__", row["tier"])
            rowhtml = rowhtml.replace("__RANK__", row["rank"])
            rowhtml = rowhtml.replace("__OFFICIAL_RANK__", row["official_rank"])
            if int(year) >= 2013:
                rowhtml = rowhtml.replace("__SPECIAL__", "<td align=\"right\">"+ row["under_18"] +"</td>\n<td align=\"right\">" + row["over_50"] + "</td>")
            else:
                rowhtml = rowhtml.replace("__SPECIAL__", "")
            individual_rounds_row = ""
            for i in range(0, individual_rounds+1):
                if i == 0:
                    individual_rounds_row += "<td align=\"right\">" + row["total_score"] + "</td>\n"
                else:
                    individual_rounds_row += "<td align=\"right\">" + row["individual_" + str(i)] + "</td>\n"
            rowhtml = rowhtml.replace("__INDIVIDUAL_ROUNDS__", individual_rounds_row)
            tablehtml += rowhtml
    html = html.replace("__TABLE__", tablehtml)
    
    html = templates.final_replace(html, "../..")
    util.writefile("../timeline/" + year + "/individual.html", html)
    
if __name__ == "__main__":
    run(sys.argv[1])
