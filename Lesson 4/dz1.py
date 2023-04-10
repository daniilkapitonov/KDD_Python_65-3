class Student:
    def_name = 'Ivan'
    def_age = 18
    def_gr_n = '10A'
    def __init__(self, name=def_name, gr_n=def_gr_n, age=def_age):
        if (name == Student.def_name):
            self.__f_name = True
        else:
            self.__f_name = False
        if (age == Student.def_age):
            self.__f_age = True
        else:
            self.__f_age = False
        if (gr_n == Student.def_gr_n):
            self.__f_gr_n = True
        else:
            self.__f_gr_n = False
        self.name = name
        self.gr_n = gr_n
        self.age = age
    
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self.age)
    def getGr_n(self):
        print(self.gr_n)

    def setNameAge(self,name, age):
        if self.__f_name:
            self.name = name
            self.__f_name = False
        else:
            print("name not def var")

        if self.__f_age:
            self.age = age
            self.__f_age = False
        else:
            print("age not def var")

    def setGr_n(self,gr_n):
        if self.__f_gr_n:
            self.gr_n = gr_n
            self.__f_gr_n = False
        else:
            print("gr_n not def var")

s1 = Student("Anna",'2A',22)
s1.getName()
s1.getGr_n()
s1.getAge()
s1.setNameAge("Masha", 23)
s1.getName()
s1.getGr_n()
s1.getAge()

s2 = Student()
s2.setNameAge("Nikita",24)
s2.getName()
s2.getGr_n()
s2.getAge()
s2.setNameAge("Nikita",24)
