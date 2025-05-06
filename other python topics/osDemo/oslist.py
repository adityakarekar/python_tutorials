import os;
folders=os.listdir("testdir") # list all files and folders in the directory
for folder in folders:
    print(os.listdir(f"testdir/{folder}")) # print the name of each file and folder

# os.getcwd() # get the current working directory