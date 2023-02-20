class Bicycle:
    name = "default"
    kg = 0
    color ="default"
    gramm = 0
    def print_param(self):
        self.gramm = self.kg * 1000
        print(self.kg, self.color, self.name, self.gramm)
    def set_name(self, name):
        self.name = name

bic_1 = Bicycle()
print(type(bic_1))
bic_1.name = "BMX"
bic_1.kg = 120
bic_1.color = "Red"
print(bic_1.kg, bic_1.color, bic_1.name)
bic_1.print_param()
bic_1.set_name("Mountains")
bic_1.print_param()

bic_2 = Bicycle()
bic_2.set_name("BMX_2")
bic_2.print_param()

mass = []
mass.append(bic_1)
mass.append(bic_2)
print(mass[0].name)