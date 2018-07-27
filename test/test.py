import os
import sys

def get_project_root():
    pgm_dir = os.path.dirname(os.path.abspath(__file__))
    print(pgm_dir)
    dir_to_rmv = pgm_dir.split(os.sep)[-1]
    print(dir_to_rmv)
    pgm_root = pgm_dir.replace(dir_to_rmv, '')
    sys.path.append(pgm_root)
    return sys.path[len(sys.path)-1]


__ini_path = get_project_root()+"framework.ini"
print(__ini_path)

s = "pripe.username"
print(s.split(".")[1])
