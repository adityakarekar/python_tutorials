#string methods

# a="Aditya!!!!!!"
# print(a.upper())
# print(a.lower())
# # print(a.rstrip("!"))
# print(a.replace("Aditya","aditya"))


a="Aditya"
# print(a.split(" "))
# print(a.capitalize())
# print(a.center(20))
# print(len(a))

# print(a.endswith("a"))


def endsWith(str):
    for i in a:
        if(i==str):
            return True
        else:
            return False
        
boolRes=endsWith("s")
print(boolRes)



# b="aabbcabcc"
# output=a4b2c

# i=1
# count=1
# count2=1
# count3=1

# for i in range(len(b)):
#     print(b[i],b[i-1])
    
#     if((b[i]==b[i-1]) and  b[i]=="a"):
#         count+=1
#     if((b[i]==b[i-1]) and  b[i]=="b"):
#         count2+=1
#     if((b[i]==b[i-1]) and  b[i]=="c"):
#         count3+=1
    
# print(f"a{count}b{count2}c{count3}")

# str1="Welcome to the console !!!"
# print(str1.endswith("to",4,10))
# print(str1.find("ome"))
# print(str1.index("ome"))

# str2="WelcomeToTheConsole123"
# print(str2.isalnum())

str="Aditya Karekar"
print(str.isprintable())
print(str.isspace())

str="ADITYA KAREKAR"
print(str.isupper())
str="aditya karekar is my name"
i=str.split(" ")
for item in i:
    print(item[0].upper()+ item[1:],end=" ")

