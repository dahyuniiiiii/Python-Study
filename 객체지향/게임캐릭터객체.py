# 플레이어의 캐릭터
# 속성: 캐릭터의 능력치, 경험치 등
# 메서드: 캐릭터를 움직이는 방법, 이동, 공격 

class Character(object): #object라는 부모 클래스에서 상속

    def __init__(self, name):
        self.name = name
        self.life = 1000 # 객체가 생성될 때 1000으로 초기화

    def attacked(self):
        self.life -= 10 #self.life를 10만큼 감소
        print("공격받음! %s 생명력 = %d" % (self.name, self.life)) #현재의 생명력 출력
        
#객체 생성, 초기 생명력 출력
a = Character("a")
b = Character("b")
c = Character("c")
#객체 속성 확인, 독립적 객체로 각 객체의 생명력은 개별적으로 관리
print("a: %d, b: %d c: %d" %(a.life, b.life, c.life))
# 공격받은 후 생명력 변화
a.attacked()
b.attacked()
a.attacked()
a.attacked()
a.attacked()
a.attacked()
a.attacked()
#최종 생명력 출력
print("a: %d, b: %d c: %d" %(a.life, b.life, c.life))