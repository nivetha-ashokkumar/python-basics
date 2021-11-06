def factorial(number1, number2):
    temp = number1
    number1 = number2
    number2 = temp
    return number1, number2


number1 = int(input("enter first value:"))
number2 = int(input("enter second vakue:"))
result = factorial(nnumber1, number2)
print("factorial is:", result)


def check(result):
    if(result != int):
        try:
            print(" given input is not integer")
        except:
            print("error")
    return result
            
