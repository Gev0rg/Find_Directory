import os
import fnmatch

def search(base, cat):
    for dirpath, dirnames, files in os.walk(base):
        if cat in dirpath and not fnmatch.fnmatch(dirpath, f'*{cat}*\\*'):
            print(dirpath)