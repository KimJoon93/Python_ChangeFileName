import os
import glob

fpath = "Put File Path in here (ex. C:\\Users\\Joon\\Desktop\\ChangeFileName\\a*.txt)"

count = 0

for fpath in glob.glob(fpath)
    fpath_r = fpath.replace('File you want to change','File name you want to change')
    os.rename(fpath,fpath_r)
    count+1

