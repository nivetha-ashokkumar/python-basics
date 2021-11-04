class shape:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        print(self.height, self.width)
class rectangle(shape):
    def __init__(self, height, width):
        super().__init__(height,width)
x = rectangle(7, 8)
x.area()
