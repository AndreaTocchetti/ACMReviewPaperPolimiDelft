import os
import time

queries = []
with open("queries_semscholar.txt", "r") as f:
    for line in f.readlines():
        queries.append(line.rstrip('\n'))

i = 1
for q in queries:
    if not os.path.exists("./semscholar_csv/q{}.csv".format(i)):
        os.system('pop8query --semscholar --max 200 --keywords=\'{}\' "./semscholar_csv/q{}.csv"'.format(q, i))
        time.sleep(5)
    else: 
        print("File q{}.csv already exists.".format(i))
    i+=1

print("= "*10, "CSV done", " ="*10)

i = 1
for q in queries:
    if not os.path.exists("./semscholar_bib/q{}.bib".format(i)):
        os.system('pop8query --semscholar --format bibtex --max 200 --keywords=\'{}\' "./semscholar_bib/q{}.bib"'.format(q, i))
        time.sleep(5)
    else: 
        print("File q{}.csv already exists.".format(i))
    i+=1

print("= "*10, "bib done", " ="*10)