class Animal:
    def __init__(self,atype,name,age):
        self.atype = atype
        self.name = name
        self.age = age

    def speak(self):
        print(f'Name: {self.name}\nAge: {self.age}')

    #def change_age(self, age):
    #    self.age = age

    #def add_weight(self,weight):
    #    self.weight = weight

#tim = Dog('Tim',30)
#rim = Dog('Rim',20)
#tim.change_age(31)
#tim.add_weight(40)
#tim.speak()
#rim.speak()
#print(f"{tim.name} weight is: {tim.weight}")

class Cat(Animal):
    def __init__(self, atype, name, age, color):
        super().__init__(atype, name, age)
        self.color = color

    def speak(self):
        print(f'Type: {self.atype}\nName: {self.name}\nAge: {self.age}\nColor: {self.color}')


bim = Cat('Cat', 'Bim' , 12, 'brown')

bim.speak()
