import os
import time

queries = []
with open("queries_semscholar.txt", "r") as f:
    for line in f.readlines():
        queries.append(line.rstrip('\n'))

i = 1
for q in queries:
    if not os.path.exists("./wos_csv/q{}.csv".format(i)):
        os.system('pop8query --wos --max 200 --keywords=\'{}\' "./wos_csv/q{}.csv"'.format(q, i))
        time.sleep(300)
    else: 
        print("File q{}.csv already exists.".format(i))
    i+=1

print("= "*10, "CSV done", " ="*10)

i = 1
for q in queries:
    if not os.path.exists("./wos_bib/q{}.bib".format(i)):
        os.system('pop8query --wos --format bibtex --max 200 --keywords=\'{}\' "./wos_bib/q{}.bib"'.format(q, i))
        time.sleep(300)
    else: 
        print("File q{}.csv already exists.".format(i))
    i+=1

print("= "*10, "bib done", " ="*10)