# 메서드 이름 앞뒤에 두개의 밑줄이 붙어있는 메서드
class Complex(object):

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
c = Complex(1, 2)
print(c)
print(str(c))