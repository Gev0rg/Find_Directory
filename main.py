from search_cat import search
from search_ree import parse_reg
from sys import argv
import win32con

name = argv[-1]

catalogs_cat = ['C:\Program Files', 'C:\Program Files (x86)']
catalogs_ree = [win32con.KEY_WOW64_32KEY, win32con.KEY_WOW64_64KEY]
ans = []

for cat in catalogs_cat:
    ans += search(cat, name)

for cat in catalogs_ree:
    ans += parse_reg(name, win32con.HKEY_LOCAL_MACHINE, cat)

ans = set(ans)

print(f'Detected {len(ans)} location{ "s" if len(ans) > 1 else "" }')

for path in ans:
    print(path)
