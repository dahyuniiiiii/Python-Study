import numpy as np
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(repr(2*a+b))
print(repr(a==2))
print(repr(b>10)) #비교연산
print(repr((a == 2) & (b > 10))) #논리연산