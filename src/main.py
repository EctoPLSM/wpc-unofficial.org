#!/usr/bin/python
# -*- coding: utf-8 -*-

import index
import e404
import timeline
import instructions
import countries
import search
import links
import static_files
import backward_compatibility

def run():
    print("Creating whole project")
    index.run()
    e404.run()
    timeline.run()
    instructions.run()
    countries.run()
    search.run()
    links.run()
    static_files.run()
    backward_compatibility.run()
    
if __name__ == "__main__":
    run()
