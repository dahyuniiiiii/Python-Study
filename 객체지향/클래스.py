#클래스 정의 (class Rectangle) - 붕어빵틀
class Rectangle(object): #Rectangle 클래스는 "사각형" 만드는 틀
    def __init__(self, h, v):  
        self.h = h  
        self.v = v  
    #메서드 정의 (def area(self))
    def area(self):  
        return self.h * self.v  
#객체 생성 -붕어빵
a = Rectangle(1, 1)   # 가로 1, 세로 1인 사각형
b = Rectangle(2, 1)   # 가로 2, 세로 1인 사각형
c = Rectangle(4, 2)   # 가로 4, 세로 2인 사각형
d = Rectangle(6, 3)   # 가로 6, 세로 3인 사각형
e = Rectangle(8, 5)   # 가로 8, 세로 5인 사각형
#객체 사용
print(a.area())
print(b.area())
print(c.area())
print(d.area())
print(e.area())