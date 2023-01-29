from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,height,base):
        self.height = height
        self.base = base
    def area(self):
        return self.base*self.height
print(issubclass(Rectangle,Shape))