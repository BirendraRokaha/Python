#tech with tim static and class methods

class Dog:
    dogs= []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    # _name is private and name is public class/method


    #class variables can be used
    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    #class variables cannot be used
    @staticmethod
    def bark(n):
        #bark n times
        for _ in range(n):
            print('Woof!')


jim = Dog("Jim")
tim = Dog('Tim')
vim = Dog('Vim')

print(Dog.num_dogs())

Dog.bark(10)
