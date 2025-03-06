# x=["Aditya",1,2,3,"Mahesh"]
# for i in x:
#     print(i)

# x=1
# y=2
# for i in range(1,4):
#     for j in range(1,3):
#         if(j==2):
#             print("X",end="")
#             break
#         print(y, end="")
#     print(x)

# for a in [1,2,3,4,"Sayali"]:
#     print(a)

from math import sqrt
for i in range(1,501):
    if(sqrt(i).is_integer()):
        print(i)

    