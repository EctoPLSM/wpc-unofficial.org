#!/usr/bin/python
import sys
import util
import templates
from database_countries import code_indexed as c_db_c
from database_countries import previous_code
from database_countries import next_code
from database_participants import code_grouped as p_db_c
from database_timeline import code_grouped as t_db_c

def run(code):
    print("Creating countries/" + code + "/index")
    html = templates.get("countries/code/index")
    html = templates.initial_replace(html, 2)
    codedata = c_db_c[code]
    
    html = html.replace("__CODE__", code)
    html = html.replace("__COUNTRY__", codedata["country"])
    
    if codedata["website"] != "":
        html = html.replace("__CONTACT_STYLE__", "")
        html = html.replace("__NATIONAL_SITE__", codedata["website"])
        if len(codedata["website"]) < 50:
            html = html.replace("__NATIONAL_SITE_TEXT__", codedata["website"])
        else:
            html = html.replace("__NATIONAL_SITE_TEXT__", codedata["website"][0:50] + "...")
    else:
        html = html.replace("__CONTACT_STYLE__", "display: none;")
        html = html.replace("__NATIONAL_SITE__", ".") # Google crawler fix
    
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
    
    if code in t_db_c:
        hostshtml = ""
        for yeardata in t_db_c[code]:
            hosthtml = templates.get("countries/code/index_host")
            if yeardata["city"] != "":
                hosthtml = hosthtml.replace("__CITY__", " - " + yeardata["city"])
            else:
                hosthtml = hosthtml.replace("__CITY__", "")
            if yeardata["homepage"] != "":
                homepagehtml = templates.get("countries/code/index_host_homepage")
                homepagehtml = homepagehtml.replace("__LINK__", yeardata["homepage"])
                hosthtml = hosthtml.replace("__HOMEPAGE__", homepagehtml)
            else:
                hosthtml = hosthtml.replace("__HOMEPAGE__", "")
            hosthtml = hosthtml.replace("__YEAR__", yeardata["year"])
            hostshtml += hosthtml
        html = html.replace("__HOST__", "<dt>WPC Host</dt>" + hostshtml)
    else:
        html = html.replace("__HOST__", "")
    
    html = templates.final_replace(html, "../..")
    util.writefile("../countries/" + code + "/index.html", html)
    
if __name__ == "__main__":
    run(sys.argv[1])
