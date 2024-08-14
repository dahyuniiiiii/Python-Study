# <for반복문 사용>
# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# answer = []
# for di in data:
#     answer.append(2 * di)
# print(answer)

import numpy as np
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = np.array(data)
print(repr(x))
print(repr(2*x)) #여러개 데이터 모두 2배
print(data*2) #리스트 길이(값x)가 정수배만큼 증가
