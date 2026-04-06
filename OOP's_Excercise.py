
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.area = Circle.pi * radius*radius

    def circum(self):
        return (2 * Circle.pi * self.radius)


circle1 = Circle(3)
print(circle1.circum())
print(f"{circle1.area}")