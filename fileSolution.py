import os

directory_path = 'C:\\Users\\adity\\OneDrive\\Desktop\\Python Tutorials\\assignmentDemo'
png_files = [file for file in os.listdir(directory_path) if file.endswith('.png')]

print(png_files)

for i in range(len(png_files)):
    os.rename(f"{directory_path}\\{png_files[i]}",f"{directory_path}\\{i+1}.png")
print("Renamed all png files in the directory.")



list1 = [1, 2, 3, 4, 5]
list2=[item for item in list1 if item%2!=0] # shallow copy
print(list2)