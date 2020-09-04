import os
import os.path
import re
import time
from datetime import datetime
import pandas as pd
import numpy as np
import xlrd
import csv

#step 1 set the working directory
os.chdir(r"\\fff\ffda\fda") #if using online path need to add r
folder_ptah = "" #the place you want to get folder then files
store = []

fold_path = os.path.join(folder_path, "GPS")
for x in range(2020,2021):
    cur_path = os.path.join(fold_path,str(x))
    sub_folders = os.listdir(cur_path)
    for s in sub_folders:
        sub_fold_path = os.path.join(cur_path,str(s))
        sub_files = os.listdir(sub_fold_path)
        if(len(sub_files)!=0):
            f_ind = -1
            f_mtime = [os.path.getmtime(os.path.join(sub_fold_path,i)) for i in sub_files]
            for ss in range(0,len(sub_files)):
                if("Final" in sub_files[ss] and "Result" in sub_files[ss]) and (".xlsx" in sub_files[ss]):
                    f_ind = ss
                    break
                if(f_ind ==-1):
                    f_ind = f_mtime.index(max(f_mtime))
                path = os.path.join(sub_fold_path,sub_files[f_ind])
                store.append(path)