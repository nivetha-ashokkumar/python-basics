def factorial(a, b):
    temp = a
    a = b
    b = temp
    return a, b
a = int(input("enter a value:"))
b = int(input("enter b vakue:"))
c = factorial(a, b)
print("factorial is:", c)
def check(c):
    if(c != int):
        try:
            print(" given input is not integer")
        except:
            print("error")
    return c
            
