# s={2,3,4,5,6,6,8,9}
# print(s)
# info={"Sayali Karekar",19,False,5.9,19}
# print(info)
# my_set=set()
# print(type(my_set))

# for value in info:
#     print(value)

s1={1,2,3}
s2={3,4,5,6,7}

#union operation
res_set=s1.union(s2)
print(res_set)

#bring all values of s2  into s1 that are not in s1
s1.update(s2)
print(s1)


#Intersection and Intersection_Update
s1={1,2,3,4,5}
s2={3,4,5,6,7,8}

# s3=s1.intersection(s2)
# print(s3)
# s1.intersection_update(s2)
# print(s1)


#Symmetric Difference: Removing all the comman elements of two sets
s3=s1.symmetric_difference(s2)
print(s3)


# Differnce: removes all the elements of s2 that are in s1
# s3=s1.difference(s2)
# print(s3)
# print(s2.issubset(s1))

# s1={1,2,3}
# s2={1,2}
# print(s2.issubset(s1))



# add a single value in a set

s1={1,2,3}
s1.add(4)

#update the set by adding multiple values
s1.update({4,5,6})
# s1.remove(4) throws an error if value is already removed
# s1.discard(4) does not throw the error for the above case
print(s1)