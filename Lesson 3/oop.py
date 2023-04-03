class Wheel:
    def __init__(self,t,price) -> None:
        self.t = t
        self.priceW = price
    def pri_all(self):
        print(self.t, self.priceW)

class Glass:
    def __init__(self,color,price) -> None:
        self.color = color
        self.priceG = price
    def pri_all(self):
        print(self.color, self.priceG)

class Car(Wheel, Glass):
    def __init__(self, t, price, color) -> None:
        Wheel.__init__(self,t=t, price=price)
        Glass.__init__(self,color, price)
        self.total_price = self.priceG + self.priceW
        self.name = "def"
        self._price = 3000000
        self.__pin = 1111

    def pin(self):
        self.__pin = 2222

    def pri_all(self):
        print('dfkjgbnnfiosdguhbfosdghb')
        Wheel.pri_all(self)
        Glass.pri_all(self)

car = Car("Winter",2300,'black')
print(car.total_price)
car.pri_all()
# car.__pin = 1111
print(car.__pin)
