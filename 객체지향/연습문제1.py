# 문제
# 삼각형의 넓이를 계산하기 위한 클래스를 만든다. 이 클래스는 다음과 같은 속성을 가진다.
# 밑변의 길이 b 와 높이 h
# 삼각형의 넓이를 계산하는 메서드 area

class Samgak: #콜론 필수
    def __init__(self, b, h): #첫번째 인자로 항상 self사용, 객체 자신을 참조하기위한 매개변수
        #객체의 속성으로 저장
        self.b = b 
        self.h = h 

    def area(self): #self를 첫번째 인자로 추가
        return 0.5 * self.b * self.h  # 삼각형의 넓이 계산

a = Samgak(10, 5)  # a.area() 호출하기위해, 먼저 'a'라는 <객체 생성>
print(a.area())  
