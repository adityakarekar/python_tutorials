def func():
    a=input("Enter a number: ")

    try:
        for i in range(1,11):
            print(f" {int(a)} X {i} = {int(a)*i}")
        return 1
    except:
        print("invalid input")
        return 0
    finally:
        print("I will always be executed")

    print("Code ends here")
x=func()
print(x)