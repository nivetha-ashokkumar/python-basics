class CamelCase:

    def __init__(self, name):
        self.name = name
        self.some()

    def some(self):
        self.name = "ashokkumar"

some = CamelCase("vijiyakumari")
print(some.name)