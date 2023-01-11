# 클래스 생성
class Circle:
    pi = 3.14

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return round(Circle.pi*self.r*self.r, 2)
    
    def circumference(self):
        return 2*Circle.pi*self.r
    
    def center(self):
        return (self.x, self.y)

# 인스턴스 생성
c1 = Circle(3, 2, 4)
print(c1.area())
print(c1.circumference())