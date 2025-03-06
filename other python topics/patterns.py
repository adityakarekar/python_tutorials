for i in range(1,6):
    for j in range(1,6):
        # print("*",end="")
        if(i==1):
           if(j==3):
               print("X",end="")
           else:
               print(" ",end="")
        elif(i==2):
            if(j%2==0):
                print("X",end="")
            else:
                print(" ",end="")
        elif(i==3):
            if(j%2!=0):
                print("X",end="")
            else:
                print(" ",end="")
        elif(i==4):
            if(j%2==0):
                print("X",end="")
            else:
                print(" ",end="")
        elif(i==5):
           if(j==3):
               print("X",end="")
           else:
               print(" ",end="")
    print()