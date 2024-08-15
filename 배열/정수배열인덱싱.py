import numpy as np
#배열 인덱스의 크기가 원래의 배열 크기와 달라도 상관없음
a = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx = np.array([0, 2, 4, 6, 8])
#idx = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
print(repr(a[idx]))