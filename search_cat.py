import os
import fnmatch

def search(basepath, catalog):
    ans = []
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_dir() and catalog.lower() in entry.name.lower():
                ans.append(basepath + '\\' + entry.name)
    return(ans)