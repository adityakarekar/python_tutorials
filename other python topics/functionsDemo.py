# def returnPersonInfo(firstName,lastName,age):
#     return {"firstname":firstName,"lastname":lastName,"myAge":age}


# myInfo=returnPersonInfo(firstName="Aditya", lastName="Karekar",age=26)
# print(myInfo)


# def printName(firstName="Aditya",lastName="Karekar"):
#     return f"{firstName} {lastName}"
# print(printName(firstName="Sayali", lastName="Salvi"))


# def printAverage(*nums):
#     sum=0
#     for i in nums:
#         sum+=i
#     return sum/len(nums)


# resultAvg=printAverage(5,6,7,6,7,8,9)
# print(resultAvg)


def printMyFullName(**name):
    print(name)
    return f"first name: {name["fName"]} last name: {name["lName"]}"

myFullName=printMyFullName(fName="Adtya",lName="Karekar")


