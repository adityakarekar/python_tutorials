
# Writing to a file one method
f=open("myFileWrite.txt","a")
f.write("Hello Aditya")
f.close()

# Writing to a file another method
with open("myFileWrite.txt","a") as f:
 f.write("Hello Aditya! \t")

f=open("myFileWrite.txt","r")
while True:
    line=f.readline()
    number=line.split(",")[0]
    if not line:
        break
    print(number)
f.close()

f=open("myFileWrite2.txt","w")
lines=["Hello Aditya\n","Hello Aditya\n","Hello Aditya\n"]
f.writelines(lines)
f.close()