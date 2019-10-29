#!/usr/bin/python
import sys
import util
import templates
from database_countries import code_indexed as c_db_c
from database_countries import previous_code
from database_countries import next_code
from database_teams import code_grouped as t_db_c
from database_participants import year_grouped as p_db_y


def run(code):
    print("Creating countries/" + code + "/team")
    html = templates.get("countries/code/team")
    html = templates.initial_replace(html, 2)
    
    html = html.replace("__CODE__", code)
    html = html.replace("__COUNTRY__", c_db_c[code]["country"])
    
    if code in previous_code:
        html = html.replace("__PREVIOUS_CODE__", previous_code[code])
        html = html.replace("__PREVIOUS_CODE_STYLE__", "")
    else:
        html = html.replace("__PREVIOUS_CODE_STYLE__", "display: none;")
        html = html.replace("__PREVIOUS_CODE__", ".") # Google crawler fix
        
    if code in next_code:
        html = html.replace("__NEXT_CODE__", next_code[code])
        html = html.replace("__NEXT_CODE_STYLE__", "")
    else:
        html = html.replace("__NEXT_CODE_STYLE__", "display: none;")
        html = html.replace("__NEXT_CODE__", ".") # Google crawler fix

    tablehtml = ""
    if code in t_db_c:
        yearhtml = ""
        lastyear = ""
        for team in t_db_c[code]:
            rowhtml = templates.get("countries/code/team_row")
            rowhtml = rowhtml.replace("__RANK__", team["rank"])
            rowhtml = rowhtml.replace("__YEAR__", team["year"])
            rowhtml = rowhtml.replace("__TEAM__", team["tier"])
            rowhtml = rowhtml.replace("__OFFICIAL_RANK__", team["official_rank"])
            contestant_number = 1
            if team["year"] in p_db_y:
                for participant in p_db_y[team["year"]]:
                    if (code == "UN" or code == participant["code"]) and participant["tier"] == team["tier"]:
                        rowhtml = rowhtml.replace("__CONTESTANT_" + str(contestant_number) + "__", participant["name"])
                        contestant_number += 1
                rowhtml = rowhtml.replace("__CONTESTANT_1__", "")
                rowhtml = rowhtml.replace("__CONTESTANT_2__", "")
                rowhtml = rowhtml.replace("__CONTESTANT_3__", "")
                rowhtml = rowhtml.replace("__CONTESTANT_4__", "")
            tablehtml += rowhtml

    html = html.replace("__TABLE__", tablehtml)
    if tablehtml == "":
        html = html.replace("__EMPTY__", "This country hasn't sent a full team.")
    else:
        html = html.replace("__EMPTY__", "")
    html = templates.final_replace(html, "../..")
    util.writefile("../countries/" + code + "/team.html", html)


if __name__ == "__main__":
    run(sys.argv[1])
