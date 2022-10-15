import os
import time

queries = []
with open("queries_scopus.txt", "r") as f:
    for line in f.readlines():
        queries.append(line.rstrip('\n'))

i = 1
for q in queries:
    if not os.path.exists("./scopus_csv/q{}.csv".format(i)):
        os.system('pop8query --scopus --keywords=\'{}\' "./scopus_csv/q{}.csv"'.format(q, i))
        time.sleep(5)
    else: 
        print("File q{}.csv already exists.".format(i))
    i+=1

print("= "*10, "CSV done", " ="*10)

for q in queries:
    if not os.path.exists("./scopus_bib/q{}.bib".format(i)):
        os.system('pop8query --scopus --format bibtex --keywords=\'{}\' "./scopus_bib/q{}.bib"'.format(q, i))
        time.sleep(5)
    else: 
        print("File q{}.csv already exists.".format(i))
    i+=1

print("= "*10, "bib done", " ="*10)