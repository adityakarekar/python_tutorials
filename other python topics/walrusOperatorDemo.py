foods=[]
#without walrus operator
# while True:
#     food=input("what food do you like?: ")
#     foods.append(food)
#     if food=="quit":
#         foods.pop()
#         break

# print(foods)

#with walrus operator
while (food := input("what food do you like: ")) != "quit":
    foods.append(food)

print(foods)