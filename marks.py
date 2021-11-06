def details(name, age, mark):
    
    if(mark>80):
        return "congrats"
    elif(mark > 60) and (mark < 80):
        return "try to do better"
    elif(mark < 60) and (mark > 40):
        return "practice more"
    else:
        return "fail"
    
    
name = input("enter your name:")
age = int(input("enter your age:"))
mark = int(input("enter your mark:"))

result = details(name, age, mark)

print(result)
    
