import math

class Circle:
    circle_count = 0
    total_square = 0
    def __init__(self, color, diametr):
        Circle.circle_count +=1
        self.color = color
        self.diametr = diametr
        self.change_square()

    def change_square(self):
        self.square = math.pi*(self.diametr**2)/2
        Circle.total_square +=self.square

    def change_color(self, color):
        self.color = color

    def change_diametr(self,diametr):
        Circle.total_square -= self.square
        self.diametr = diametr
        self.change_square()

c1= Circle('Red', 30)   
c2= Circle('White', 20)   
c3= Circle('Green', 10)   
c4= Circle('Blue', 5)   
c5= Circle('Brown', 2)        

print(c4.square, c4.color, c4.diametr)
print(Circle.circle_count, Circle.total_square)
c4.change_diametr(40)
print(Circle.circle_count, Circle.total_square)
c4.change_diametr(5)
print(Circle.circle_count, Circle.total_square)