data={1:"Aditya",2:"Sayali",3:"mahesh"}

# 1:Key should be a unique data type that is immutable in python like string and number
# "Aditya":Value of dictionary
print(data.get(4,"Not Found"))
print(data)
keys=['Aditya','Mahesh','Mayur']
values=['javascript','SAP','JAVA']


# Combining keys and values to create a dictionary
newData=dict(zip(keys,values))
print(newData["Mayur"])
newData["Sayali"]="C#"
print(newData)

prog={"JS":"VS Code",
      "CSS":"Atom",
      "Python":["Sublime","PyCharm"],
      "JAVA":{"JRE":"Eclipse","JEE":"JetBrains IDE"}}

print(prog["JAVA"]["JEE"])
