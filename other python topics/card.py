str1="1234567891011"
print(str1)

print(str1[5])
newlist = []

for i in range(len(str1)):
    if i<8:
        newlist.append(str1[i])
    if i>8:
        newlist.append("*")
print("".join(newlist))