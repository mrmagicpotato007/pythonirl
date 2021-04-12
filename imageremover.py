import os
import shutil
from PIL import  Image

target="C:/Users/harsha/Downloads/jpg"
os.chdir(target)

a=os.listdir(".")

for file in a:
    os.makedirs("Trash",exist_ok=True)
    try:
        Image.open(file)
    except Exception as e:
        shutil.move(file,"Trash")

