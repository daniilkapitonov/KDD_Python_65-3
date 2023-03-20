class Wall:
    color = ""
    heigh = 0
    lenght = 0
    area_wall = 0
    def __init__(self, c="White",h=120,l=80):
        self.color = c
        self.heigh = h
        self.lenght = l
        self.area_wall = self.heigh * self.lenght
    def print_param_wall(self):
        print(self.color, self.area_wall)

class House(Wall):
    number = 0
    def __init__(self, c="White", h=120, l=80, num = 1):
        self.number = num
        super().__init__(c, h, l)
    def print_house(self):
        print("My house is:")
        self.print_param_wall()
        print(self.number)

w1 = Wall(l=2)
w1.print_param_wall()

h1 = House()
h1.print_house()


