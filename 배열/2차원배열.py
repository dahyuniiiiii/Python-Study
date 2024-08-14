import numpy as np
c = np.array([[0, 1, 2], [3, 4, 5]])  #안쪽 리스트 길이 : 열(가로), 바깥쪽 리스트 길이 : 행(세로)
print(repr(c))
print(len(c)) #행의개수
print(len(c[0])) #열의 개수