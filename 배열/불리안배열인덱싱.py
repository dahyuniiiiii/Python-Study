import numpy as np
#인덱스 배열의 크기가 원래의 객체의 크기와 같아야함
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
idx = np.array([True, False, True, False, True,False, True, False, True, False])
print(repr(a[idx]))
print(repr(a % 2))
print(repr(a%2==0))
print(repr(a[a%2==0]))