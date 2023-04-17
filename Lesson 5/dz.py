import codecs

class Person:
    def __init__(self, name, age,number, address) -> None:
        self.name = name
        self.age = age
        self.number = number
        self.address = address
        
    def __str__(self):
        return f"Инофрмация о человеке:\nИмя - {self.name}\nВозраст - {self.age}\nНомер - {self.number}\nАдрес - {self.address}\n"

class Book:
    def __init__(self, per_list = []) -> None:
        self.per_list = per_list

    def add_people(self, people:Person):
        self.per_list.append(people)

    def add_people_list(self, p_list):
        for i in p_list:
            self.add_people(i)

    def remove(self, p:Person):
        cash = 0
        for per in self.per_list:
            if per == p:
                cash = self.per_list.index(p)
        self.per_list.pop(cash)

    def find_by_street(self,street):
        cash = []
        for p in self.per_list:
            if p.address == street:
                cash.append(p)
        return cash
    
    def to_txt(self, file_name = r"Lesson 5/book.txt"):
        f = codecs.open(file_name, "w+",'utf-8')
        f.write(str(self))
        f.close()
    
    def __str__(self):
        return "Список людей в записной книге:\n"+"".join(list(map(str,self.per_list)))
              

p1 = Person("Vova", 21, 4, "vavilova")
p2 = Person("Peta", 20, 7, "novay")
p3 = Person("Masha", 24, 1, "bas")
p4 = Person("Polina", 16, 2, "street")
p5 = Person("Anna", 22, 9, "vavilova")
b = Book([p1,p2,p3,p4,p5])
print(b)
print('del')
b.remove(p2)
print(b)

print("res of search")
ser = b.find_by_street('vavilova')
for i in ser:
    print(i)

b.to_txt()