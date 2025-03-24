# tup=(1,2,3,4,5,6,7,8,9)
# # tup[0]=23
# key=7
# for i in range(0,len(tup)):
#     if(tup[i]==key):
#         print(i)
#         break

tup=("India","Russia","China","Japan")
countriesList=list(tup)
countriesList.append("Ukraine")
tup=tuple(countriesList)
print(tup)


tup2=(1,2,3,4,5,6,7,3,9)
res=tup2.index(3,2,len(tup)-1)
print(res)