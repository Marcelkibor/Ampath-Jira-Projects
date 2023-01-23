#Open-Closed Principal. The shape class can be extended to other classes but can't be modified
class Shape:
    def __init__(self, color):
        self.color = color
#  you can add more properties than can be extended to this superclass.
class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height
    def area(self):
        return "Rectangle area->",self.width * self.height

class Triangle(Shape):
    def __init__(self, color, base,height):
        super().__init__(color)
        self.height = height
        self.base = base
    def area(self):
        area = 1/2*self.base * self.height
        return "Triangle ->",area

callTriangle = Triangle("red",10,10)
print(callTriangle.area())
callRectangle = Rectangle(10,10,"red")
print(callRectangle.area())