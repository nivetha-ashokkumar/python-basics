def sum(*arguments, **keywordarguments):
    sum = arguments1 + keywordarguments1
    return sum

arguments1 = int(input("enter arguments value:"))
keywordarguments1 = int(input("enter keywordarguments value:"))

result = sum(arguments1, keywordarguments1)
print(result)
