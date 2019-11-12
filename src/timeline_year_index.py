#!/usr/bin/python

import sys
import util
import templates
from database_timeline import year_indexed as t_db_y
from database_timeline import previous_year
from database_timeline import next_year
from database_countries import code_to_country
from database_participants import year_grouped as p_db_y
from database_rounds import year_grouped as r_db_y
from config import next_year as ny

def run(year):
    print("Creating timeline/" + year + "/index")
    html = templates.get("timeline/year/index")
    html = templates.initial_replace(html, 1)
    yeardata = t_db_y[year]
    html = html.replace("__YEAR__", year)
    html = html.replace("__NUMBER__", yeardata["number"])
    html = html.replace("__ORDINAL__", util.ordinal(yeardata["number"]))
    html = html.replace("__DATE__", yeardata["date"])
    html = html.replace("__CODE__", yeardata["code"])
    html = html.replace("__COUNTRY__", code_to_country[yeardata["code"]])
    
    if "code2" in yeardata:
        html = html.replace("__CODE2__", yeardata["code2"])
        html = html.replace("__COUNTRY2__", code_to_country[yeardata["code2"]])
        html = html.replace("__CODE2_STYLE__", "")
    else:
        html = html.replace("__CODE2_STYLE__", "display: none;")
        html = html.replace("__CODE2__", ".") # Google crawler fix
    
    if yeardata["city"] != "":
        html = html.replace("__CITY__", yeardata["city"] + ",")
    else:
        html = html.replace("__CITY__", "")
    
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
    
    if yeardata["p_contestant"] != "":
        html = html.replace("__P_CONTESTANT_STYLE__", "")
        html = html.replace("__P_CONTESTANT__", yeardata["p_contestant"])
    else:
        html = html.replace("__P_CONTESTANT_STYLE__", "display: none;")
    
    if yeardata["p_team"] != "":
        html = html.replace("__P_TEAM_STYLE__", "")
        html = html.replace("__P_TEAM__", yeardata["p_team"])
    else:
        html = html.replace("__P_TEAM_STYLE__", "display: none;")
    
    if yeardata["homepage"] != "":
        html = html.replace("__HOMEPAGE_STYLE__", "")
        html = html.replace("__HOMEPAGE__", yeardata["homepage"])
    else:
        html = html.replace("__HOMEPAGE_STYLE__", "display: none;")
        html = html.replace("__HOMEPAGE__", ".") # Google crawler fix

    if year == ny:
            html = html.replace("__BOOKLET__", " ")
    elif int(year) in range(1992, 1998) or int(year) in [2000, 2001, 2007, 2010]:
            html = html.replace("__BOOKLET__", "missing")
    else:
            html = html.replace("__BOOKLET__", "<a href = \"../../pdfs/WPC " + year + ".pdf\">PDF</a>")

    tablehtml = ""
    flag_special = False
    flag_cancel = False
    flag_unknown = False
    if year in r_db_y:
        for row in r_db_y[year]:
            rowhtml = templates.get("timeline/year/round_row")
            rowhtml = rowhtml.replace("__DAY__", row["day"])
            rowhtml = rowhtml.replace("__TIME__", row["time"])
            rowhtml = rowhtml.replace("__NUMBER__", row["number"])
            rowhtml = rowhtml.replace("__TYPE__", row["type"])
            rowhtml = rowhtml.replace("__NAME__", row["name"])
            rowhtml = rowhtml.replace("__DURATION__", row["duration"] + " min")
            rowhtml = rowhtml.replace("__POINTS__", row["points"] + " points")
            tablehtml += rowhtml
            if "*" in row["points"]:
                flag_special = True
            if "#" in row["points"]:
                flag_cancel = True
            if "?" in row["points"]:
                flag_unknown = True
            if "?" in row["duration"]:
                flag_unknown = True    
    html = html.replace("__TABLE__", tablehtml)
   
    if flag_special:
        html = html.replace("__SPECIAL__", "* This round adopted a scoring system whose maximum score couldn't be defined. The score of best individual or team is shown instead.<br>")
    else:
        html = html.replace("__SPECIAL__", "")

    if flag_cancel:
        html = html.replace("__CANCEL__", "# This round had been cancelled for various reasons.<br>")
    else:
        html = html.replace("__CANCEL__", "")
    
    if flag_unknown:
        html = html.replace("__UNKNOWN__", "Some information are missing from this table. If you can fill in the blank, please contact the webmaster: <a href=\"mailto:__WEBMASTER__\">__WEBMASTER__</a>.<br>")
    else:
        html = html.replace("__UNKNOWN__", "")

    html = templates.final_replace(html, "../..")
    util.writefile("../timeline/" + year + "/index.html", html)
    
if __name__ == "__main__":
    run(sys.argv[1])
