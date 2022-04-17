import os
import fnmatch

def search(base, cat):
    for dirpath, dirnames, files in os.walk(base):
        if cat.lower() in dirpath.lower() and not fnmatch.fnmatch(dirpath, f'*{cat}*\\*'):
            print(dirpath)
