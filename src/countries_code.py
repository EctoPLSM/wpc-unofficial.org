#!/usr/bin/python
import sys
import util
import countries_code_index
import countries_code_individual
import countries_code_team

def run(code):
    print("Creating countries/" + code)
    util.makedirs("../countries/" + code)
    countries_code_index.run(code)
    countries_code_individual.run(code)
    countries_code_team.run(code)
    
if __name__ == "__main__":
    run(sys.argv[1])
