a=int(input("Enter a value between 5 and 9: "))
if(str(a).lower()=="quit"):
    print("Program ends here")
if(a>5 or a<9):
    raise ValueError("Value should be in between 5 and 9")
