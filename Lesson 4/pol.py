import copy

class Water:
    def __init__(self, amount=0, name = 'Water') -> None:
        self.amount = amount
        self.name = name

    def __add__(self, other):
        cash = copy.copy(self)
        # cash = self
        cash.amount = self.amount + other.amount
        return cash
        # return "Ну ты коечно МДА"

    def __mul__(self,other):
        cash = copy.copy(self)
        # cash = self
        cash.amount = self.amount * other.amount
        return cash
    
    def __str__(self):
        return f"Amount = {self.amount}, name = {self.name}"

b1 = Water(1, "w1")
b2 = Water(2, 'w2')
b3 = b1+b2
b4 = b2*b3
# print(b3)
print(b3.amount)
print(b3.name)
print(b1,b3)
print(b4.amount)