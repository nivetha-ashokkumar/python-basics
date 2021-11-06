def sum(*args, **kwargs):
    sum = args1 + kwargs1
    return sum

args1 = int(input("enter args value:"))
kwargs1 = int(input("enter kwargs value:"))

result = sum(args1, kwargs1)
print(result)
