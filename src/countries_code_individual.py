#!/usr/bin/python
import sys
import util
import templates
from database_countries import code_indexed as c_db_c
from database_countries import previous_code
from database_countries import next_code
from database_participants import code_grouped as p_db_c
from database_participants import database as p_db


def run(code):
    print("Creating countries/" + code + "/individual")
    html = templates.get("countries/code/individual")
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
    if code in p_db_c:
        yearhtml = ""
        lastyear = ""
        for participant in p_db_c[code]:
            rowhtml = templates.get("countries/code/individual_row")
            rowhtml = rowhtml.replace("__NAME__", participant["name"])
            rowhtml = rowhtml.replace("__RANK__", participant["rank"])
            rowhtml = rowhtml.replace("__YEAR__", participant["year"])
            rowhtml = rowhtml.replace("__TEAM__", participant["tier"])
            rowhtml = rowhtml.replace("__OFFICIAL_RANK__", participant["official_rank"])  
            tablehtml += rowhtml
    elif code == "UN":
        for participant in p_db:
            if "UN" in participant["tier"]:
                rowhtml = templates.get("countries/code/individual_row")
                rowhtml = rowhtml.replace("__NAME__", participant["name"])
                rowhtml = rowhtml.replace("__RANK__", participant["rank"])
                rowhtml = rowhtml.replace("__YEAR__", participant["year"])
                rowhtml = rowhtml.replace("__TEAM__", participant["tier"])
                rowhtml = rowhtml.replace("__OFFICIAL_RANK__", participant["official_rank"])  
                tablehtml += rowhtml

    html = html.replace("__TABLE__", tablehtml)
    html = templates.final_replace(html, "../..")
    util.writefile("../countries/" + code + "/individual.html", html)


if __name__ == "__main__":
    run(sys.argv[1])
