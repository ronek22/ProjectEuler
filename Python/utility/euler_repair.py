'''Script to add problem subject to head of the Project Euler solutions'''
import requests
from lxml import html
from math import ceil
from glob import glob

def count_solutions():
    files = []
    for py in glob('*.py'):
        files.append(py)
    return files,len(files)-1

def write_begining(file, problem):
    f = open(file,'r+')
    lines = f.readlines() # read old content
    f.seek(0) # go back to the beginning of the file
    f.write("'''"+problem+"'''\n") # write new content at the beginning
    for line in lines: # write old content after new
        f.write(line)
    f.close()


files,count = count_solutions()
files_names = [x[3:] for x in files]
print count
pages = int(ceil(count / 50.0))
print pages
file_id = 0


for i in range(1,pages+1):
    r = requests.get("https://projecteuler.net/archives;page="+str(i))
    print r.url
    page = html.fromstring(r.content)


    problems = page.xpath("//a[contains(@href, 'problem')]/text()")

    for p in problems:
        if(file_id > count):
            break
        else:
            write_begining(files_names[file_id], p)
            file_id += 1
