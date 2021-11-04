class operation:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def outputvalues(self):
        vals = (self.number1, self.number2)
        return vals
c1 = operation(10, 20)
print(c1.outputvalues())

    