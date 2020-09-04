import os
import os.path
import re
import time
from datetime import datetime
from distutils.dir_util import copy_tree
def copy_valid_folder():
    os.chdir(r"\\eeee\Lars\results")
    #Above specify the working directory to get files
    current_year = datetime.now().year
    current_year = str(current_year)
    start_path = r"\\elw16..\Lars\Results"
    path_ = os.path.join(start_path,current_year)
    end_path = r"\\elw16..\Lars\Results\end"
    sub_dirs = os.listdir(path_)
    for folder in sub_dirs:
        if 'ssst' in folder:
            fromDirec = os.path.join(path_,folder)
            toDirec = os.path.join(end_path,current_year,folder)
            copy_tree()
        else:
            continue
copy_valid_folder()