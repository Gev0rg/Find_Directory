from search import search
from sys import argv

catalog = argv[1]

for basepath in ('C:\Program Files', 'C:\Program Files (x86)'): 
    search(basepath, catalog)

