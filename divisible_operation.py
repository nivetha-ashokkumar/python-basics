number = int(input("enter positive number"))

if(number % 2 == 0 or number % 3 == 0 or number % 5 == 0):
    print("the given number is divisible by 2 or 3 or 5")
else:
    print("the given number is not divisible by 2 or 3")
