import os
import shutil

target = "C:/Users/harsha/Downloads"
os.chdir(target)

filenames = os.listdir(".")

for file in filenames:
    extname=(file.split(".")[-1])
    os.makedirs(extname,exist_ok=True)
    shutil.move(file,os.path.join(extname,file)) #in windows it will be  so we use os.path

