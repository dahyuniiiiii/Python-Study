# 객체지향 사용하는 이유
# 재사용성: 코드 재사용에 뛰어남 
# 유지보수 용이: 수정이 필요할 때 특정 클래스만 수정하면 됨 
# 확장성: 상속과 다형성을 통해 쉽게 확장가능
# 캡슐화: 객체는 내부 상태를 숨기고 메서드를 통해 접근하도록 함

class Rectangle(object):  # 'Rectangle' 클래스를 정의
    def __init__(self, h, v):  # 객체의 초기 상태를 설정, h와 v를 받아 인스턴스 변수로 저장
        self.h = h  # 인스턴스 변수 self.h에 h 값을 저장, 캡슐화
        self.v = v  # 인스턴스 변수 self.v에 v 값을 저장, 캡슐화

    def area(self):  # 넓이를 계산하는 메서드 정의
        return self.h * self.v  # 인스턴스 변수 h와 v를 곱해 반환, 코드 재사용

# Rectangle 클래스의 인스턴스를 생성하고, r이라는 변수에 저장
r = Rectangle(10, 20) #r이 객체
# r 인스턴스의 area 메서드를 호출해 넓이를 계산하고, a에 저장
a = r.area()
print(a)
print(r.h) #속성 꺼내려면 객체 이름 뒤에 점(.)을 붙인 다음 속성 이름 입력
print(r.v)