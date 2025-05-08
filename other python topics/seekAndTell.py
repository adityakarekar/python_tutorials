with open("myFileWrite2.txt","r") as f:
    print(type(f))

    f.seek(4) # Move the cursor to the 5th byte in the file
    print(f.tell()) # Print the current position of the cursor in the file
    char=f.read(5) # Read 5 bytes from the file
    print(char) # Print the characters read from the file

with open("file.txt","w") as f:
    f.write("Hello Aditya")
    f.truncate(5)   # Truncate the file to 5 bytes


with open("file.txt","r") as f:
    print(f.read())