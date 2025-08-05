import os
folderPath=r"C:/Users/adity/OneDrive/Desktop/Python Tutorials/other python topics/clearTheClutterDemo"
print(os.path.abspath(__file__))
allFiles=os.listdir(folderPath)
print(allFiles)
txtFiles=[file for file in allFiles if file.endswith(".txt")]

for i in range(len(txtFiles)):
    os.rename(os.path.join(folderPath,txtFiles[i]),os.path.join(folderPath,f"{i+1}.txt"))
