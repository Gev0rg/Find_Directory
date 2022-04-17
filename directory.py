from itertools import count
from tokenize import Name
from typing import Counter
from unicodedata import name
from search_cat import search
from search_ree import parse_reg
from sys import argv
import win32con

name = argv[-1]

pf_cat = search('C:\Program Files', name)
pfx86_cat = search('C:\Program Files (x86)', name)
pf = parse_reg(name, win32con.HKEY_LOCAL_MACHINE, win32con.KEY_WOW64_32KEY)
pfx86 = parse_reg(name, win32con.HKEY_LOCAL_MACHINE, win32con.KEY_WOW64_64KEY)

print(f'Detected {len(pf_cat) + len(pfx86_cat) + len(pf) + len(pfx86)} location{ "s" if len(pf_cat) + len(pfx86_cat) + len(pf) + len(pfx86) > 1 else "" }')

for path in pf_cat + pfx86_cat + pf + pfx86:
    print(path)
