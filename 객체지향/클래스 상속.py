class Character(object):

    def __init__(self, name):
        # 모든 캐릭터는 이름과 생명력(life)을 가짐
        self.name = name
        self.life = 1000 # 객체가 생성될 때 1000으로 초기화

    def attacked(self):
        # 캐릭터가 공격을 받았을 때 생명력을 10만큼 감소
        self.life -= 10 #생명력 감소
        print("공격받음! %s 생명력 = %d" % (self.name, self.life))
#Character 클래스 상속
class Warrior(Character):

    def __init__(self, name):
        # 부모 클래스(Character)의 초기화 코드를 호출하여 name과 life를 초기화
        super(Warrior, self).__init__(name)
        #super()함수를 사용해 부모 클래스의 __init__ 메서드를 호출하고 부모 클래스에서 정의한 name과 life 속성을 초기화
        #각각 부모 클래스에서 정의된 속성 외에, 자신만의 속성(strength, intelligence)을 추가로 정의
        self.strength = 15
        self.intelligence = 5

#Character 클래스 상속
class Wizard(Character):

    def __init__(self, name):
        # 부모 클래스(Character)의 초기화 코드를 호출하여 name과 life를 초기화
        super(Wizard, self).__init__(name)
        #super()함수를 사용해 부모 클래스의 __init__ 메서드를 호출하고 부모 클래스에서 정의한 name과 life 속성을 초기화
        #각각 부모 클래스에서 정의된 속성 외에, 자신만의 속성(strength, intelligence)을 추가로 정의
        self.strength = 5
        self.intelligence = 15

# Warrior 클래스의 객체를 생성 - 이름은 "Warrior1"
a = Warrior("Warrior1")
# Wizard 클래스의 객체를 생성 - 이름은 "Wizard1"
b = Wizard("Wizard1")

# 각각의 캐릭터의 초기 생명력을 출력
print(a.life, b.life)  
# 각각의 캐릭터의 힘을 출력
print(a.strength, b.strength)  
# 각각의 캐릭터의 지능을 출력
print(a.intelligence, b.intelligence) 

#attacked() 메서드는 Character 클래스에서 정의되었으며, 이 메서드는 모든 자식 클래스에서 동일하게 작동
a.attacked() 
b.attacked() 
#attacked() 메서드는 호출된 객체의 life 속성을 감소시키고, 현재 생명력을 출력