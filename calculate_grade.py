class calculate:
    def __init__(self, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        
values = calculate(80, 70, 76)

print(values.mark1)
print(values.mark2)
print(values.mark3)

total_mark = values.mark1 + values.mark2 + values.mark3
average = total_mark/3

print(total_mark)
print(average)

def grade(mark):
    if(mark>=80):
        return "your grade is 0"
    elif(mark >= 60) and (mark < 80):
        return "your grade is a"
    elif(mark < 60) and (mark >= 40):
        return "your grade is b"
    else:
        return "fail"
    
mark = int(input("enter your mark:"))
result = grade(mark)
print(result)
    


        


