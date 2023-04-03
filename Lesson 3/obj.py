class Car:
    car_count = 0
    mass_car = []
    def __init__(self):
        Car.car_count +=1
        Car.mass_car.append(self)
        self.name = "Def"
    @staticmethod
    def asd():
        i=0
        
    @classmethod
    def cl(cls):
        print(cls.__name__)
        print(cls.car_count)
        print(cls.mass_car)

    def st():
        i=0
        
c1 = Car()
c2 = Car()
c3 = Car()
c4 = Car()
c5 = Car()

print(c3.car_count)
print()
Car.cl()
print(c4.name)
Car.mass_car[3].name = "Mazda"
print(c4.name)