# 문제
# 사각 기둥의 부피를 계산하기 위한 클래스를 만든다. 이 클래스는 다음과 같은 속성을 가진다.
# 밑면의 가로 길이 a, 밑면의 세로 길이 b, 높이 h
# 부피를 계산하는 메서드 volume
# 겉넓이를 계산하는 메서드 surface

class Sagak:
    def __init__(self, a, b, h): #콜론 필수
        self.a = a
        self.b = b
        self.h = h
    
    def volume(self): 
        # 부피 계산
        return self.a * self.b * self.h # 메서드 내에서 계산한 값을 반환
    
    def surface(self):
        # 겉넓이 계산
        return 2 * (self.a * self.b + self.a * self.h + self.b * self.h)

# 객체 생성
s = Sagak(3, 4, 5)
print("부피:", s.volume()) 
print("겉넓이:", s.surface())  

# self는 메서드 내부에서 값을 할당하거나 계산하는 대상이 아님
