import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-np.pi, np.pi, 256) #-π부터 π까지 256개의 점을 생성
C = np.cos(X) #X의 각 점에서의 코사인 값을 계산
plt.title("tick label") #틱=눈금
plt.plot(X, C) #선 그래프 그림
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi]) #x축의 틱 위치와 레이블 설정
#-π, -π/2, 0, π/2, π에 대한 틱 위치를 설정하고, 해당 위치에 표시할 레이블을 설정
plt.yticks([-1, 0, +1]) #y축의 틱 위치를 -1, 0, +1로 설정
plt.grid(True) #그리드선 표시,제거
plt.show()