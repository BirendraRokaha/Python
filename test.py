#python oop
#define a class
class Employee:
    no_employee = 0
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.email=fname +'_'+ lname +'@empo.com'
        Employee.no_employee += 1
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def display(self):
        print(f'Name :{self.fname} {self.lname}')
        print(f'Pay :{self.pay}')
        print(f'Email :{self.email}')

e_1 = Employee("Biren","Rokaha",4000)
e_2 = Employee("Ram","Sham",40000)


e_1.display()
e_2.display()

print(Employee.no_employee)



fname = input('Enter first name: ')
lname = input('Enter last name: ')
pay = int(input('Enter the pay: '))
e_3 = Employee(fname,lname,pay)
e_3.display()



