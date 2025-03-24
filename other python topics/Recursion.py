# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n* factorial(n-1)
    

# res=factorial(5)
# print(res)


def fib(n:int):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1)+ fib(n-2)
    

print(fib(6))