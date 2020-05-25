#tech with tim overloading methods
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x,self.y)

    def move(self, x,y):
        self.x +=x
        self.y +=y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __str__(self):
        return '(' +str(self.x)+','+str(self.y)+ ')'
    def length(self):
        import math
        return math.sqrt(self.x**2 |self.y**2)

    def __gt__(self, p):
        return self.length() > p.length()

p1 = Point(3,4)
p2 = Point(4,5)
p3 = Point(1,2)
p4 = Point(0,1)
p5 = p1+p2
p6 = p1-p2
print(p5,p6)

print(p1 > p2)

print(p1.length(),p3.length())

