info={"name":"Aditya","age":26,"eligible":True}
print(info.keys())

for key in info.keys(): 
    print(info[key])


print(info.items())

for key,value in info.items():
    print(f"{key}:{value}")



ep1={122:56,134:69,222:89}
ep2={112:66,138:89,222:89}

ep1.pop(122)
# ep1.update(ep2)
print(ep1)