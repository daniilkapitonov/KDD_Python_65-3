class Ball:
    def __init__(self, size =0, t = "def",col = "red") -> None:
        self.size = size
        self.type = t
        self.color = col
        self.weight = self.size*30

    def change_col(self,col):
        self.color = col

    def change_size(self,size):
        self.size = size
        self.change_weight()
    
    def change_weight(self):
        self.weight = self.size*30


b1 = Ball(34,"Football","Blue")
b2 = Ball(74,"BasketBall","Red")
print(b1.size,b1.color,b1.type, b1.weight)
b1.change_col("white")
b1.change_size(68)
print(b1.size,b1.color,b1.type, b1.weight)
print(b1.size,b1.color,b1.type)
print(b2.size,b2.color,b2.type)