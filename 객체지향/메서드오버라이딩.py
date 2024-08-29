class Character(object):

    def __init__(self):
        self.life = 1000
        self.strength = 10
        self.intelligence = 10

    def attacked(self):
        self.life -= 10
        print("공격받음! 생명력 =", self.life)

    def attack(self):
        print("공격!")
class Warrior(Character):

    def __init__(self):
        super(Warrior, self).__init__() #Character 클래스의 __init__ 메서드가 실행되며, life = 1000, strength = 10, intelligence = 10으로 초기화
        #super()를 사용함으로써, 부모 클래스에서 이미 정의된 속성과 메서드를 자식 클래스가 사용할 수 있게 하며, 동시에 필요한 경우 자식 클래스에서 속성을 변경함
        self.strength = 15
        self.intelligence = 5

    def attack(self):
        print("육탄 공격!")
class Wizard(Character):

    def __init__(self):
        super(Wizard, self).__init__()
        self.strength = 5
        self.intelligence = 15

    def attack(self):
        print("마법 공격!")
a = Character()
b = Warrior()
c = Wizard()
a.attack()
b.attack()
c.attack()
a.attacked()
b.attacked()