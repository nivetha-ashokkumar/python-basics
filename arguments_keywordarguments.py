def sum(*arguments, **keywordarguments):
    sum = arguments1 + keywordarguments1
    return sum

arguments1 = int(input("enter args value:"))
keywordarguments1 = int(input("enter kwargs value:"))

result = sum(arguments1, keywordarguments1)
print(result)
