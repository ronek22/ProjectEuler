'''Script to create readme for github project'''
import requests
from lxml import html
from math import ceil
from glob import glob

def count_solutions():
    files = []
    for py in glob('../*.py'):
        files.append(py)
    return files,len(files)-1

LINK_TO_PYTHON = "Python/"
files,count = count_solutions()
files_names = [x[3:] for x in files]

print(files_names)
print(count)
pages = int(ceil(count / 50.0))
print(pages)
file_id = 0

FILE_README = open("../../README.md", 'w')
FILE_README.write("# PROJECT EULER\nExercises from Project Euler, just for training algorithms and python.\n")



for i in range(1,pages+1):
    r = requests.get("https://projecteuler.net/archives;page="+str(i))
    print(r.url)
    page = html.fromstring(r.content)


    problems = page.xpath("//a[contains(@href, 'problem')]/text()")

    for p in problems:
        if(file_id > count):
            break
        else:
            FILE_README.write("["+str(file_id+1)+". "+p+"]("+LINK_TO_PYTHON+files_names[file_id]+")\n\n")
            file_id += 1
