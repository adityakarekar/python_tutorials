import shutil
import os

filePath=os.path.join(os.getcwd(),"other python topics","shUtilDemo.py")
print(filePath)
shutil.copy(filePath,"other python topics/copyOfShUtilDemo.py")