#!/usr/bin/python
import config
from config import next_year
import templates
import util
from database_countries import code_to_country
from database_timeline import database as t_db

def run():
    print("Creating instrucitons")
    util.makedirs("../instructions")
    html = templates.get("instructions/index")
    html = templates.initial_replace(html, 4)
    
    tablehtml = ""
    upcominghtml = ""
    for row in t_db:
        rowhtml = templates.get("instructions/index_row")
        rowhtml = rowhtml.replace("__YEAR__", row["year"])
        if row["year"] == next_year:
            rowhtml = rowhtml.replace("__BOOKLET__", " ")
            rowhtml = rowhtml.replace("__NOTE__", " ")
        if int(row["year"]) in range(1992, 1998) or int(row["year"]) in [2000, 2001, 2007, 2010]:
            rowhtml = rowhtml.replace("__BOOKLET__", " ")
            rowhtml = rowhtml.replace("__NOTE__", "missing")
        else:
            rowhtml = rowhtml.replace("__BOOKLET__", "<a href = \"../pdfs/WPC " + row["year"] + ".pdf\">PDF</a>")
        if row["year"] == "1999":
            rowhtml = rowhtml.replace("__NOTE__", "partial")
        else:
            rowhtml = rowhtml.replace("__NOTE__", " ")
        if int(row["year"]) <= int(config.next_year) + 2:
            # Reverse list
            tablehtml = rowhtml + tablehtml
        else:
            upcominghtml = rowhtml + upcominghtml
    html = html.replace("__TABLE__", tablehtml)
    
    html = templates.final_replace(html, "..")
    util.writefile("../instructions/index.html", html)
    
if __name__ == "__main__":
    run()
