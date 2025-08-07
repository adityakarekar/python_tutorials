import time
# def usingWhile():
#     i=0
#     while i<50000:
#         i+=1
#         print(i)


# def usingFor():
#     for i in range(50000):
#         print(i)

# init=time.time()
# tFor=time.time()-init
# usingFor()
# init=time.time()
# tWhile=time.time()-init
# usingWhile()
# print(f"{tFor} seconds for for loop")
# print(f"{tWhile} seconds for while loop")

# print(4)
# time.sleep(2) 
# print("this was printed after 2 seconds of sleep")

t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(f"Current time is: {formatted_time}")

