#!/usr/bin/python
import subprocess

def run():
    print("Copying static files")
    # shutils pls no :(
    subprocess.Popen("copy -r ./templates/img ../", shell=True)
    subprocess.Popen("copy -r ./templates/css ../", shell=True)
    subprocess.Popen("copy -r ./templates/pdfs ../", shell=True)


if __name__ == "__main__":
    run()
