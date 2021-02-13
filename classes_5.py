
#Dunder Methods(Var olan ve değiştirilebilen methodlar)

class Circle:
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*self.pi

    def __repr__(self):
        return f"{__class__.__name__} object with {self.radius} radius"
    
    def __len__(self):
        return self.radius

circle_2 = Circle(10)
print(len(circle_2))

print(dir(circle_2))

print(4 + 8)
print(int.__add__(4,8))

