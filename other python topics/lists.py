
# lists are used to store multiple values and are mutable(can be changed) 
nums=[1,2,3,4,5,6,7,8,9]
print(nums[0:])

values=[1.2,"aditya"]
print(values)

mil=[nums,values]

nums.append(45)
nums.insert(2,77)
nums.remove(77)
nums.pop(3)
nums.pop()
del nums[1:]
nums.extend([2,3,4,5,6,7,8,9])
print(nums)
print(min(nums))
print(max(nums))
print(nums.sort())
# print(mil)