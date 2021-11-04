class calculate:
    def __init__(self, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
c1 = calculate(80, 70, 76)
print(c1.mark1)
print(c1.mark2)
print(c1.mark3)
total_mark = c1.mark1 + c1.mark2 + c1.mark3
avg = total_mark/3
print(total_mark)
print(avg)