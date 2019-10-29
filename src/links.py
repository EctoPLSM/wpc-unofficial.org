#!/usr/bin/python
import util
import templates

def run():
    print("Creating links")
    util.makedirs("../links")
    html = templates.get("links/index")
    html = templates.initial_replace(html, 6)
    html = templates.final_replace(html, "..")
    util.writefile("../links/index.html", html)
    
if __name__ == "__main__":
    run()
