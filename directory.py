from search import search

catalog = input()

for basepath in ('C:\Program Files', 'C:\Program Files (x86)'): 
    search(basepath, catalog)

