import matplotlib.pylab as plt
import numpy as np
N = 30 #데이터 포인트 개수 설정
np.random.seed(0)
#0과 1 사이의 난수 30개를 생성
x = np.random.rand(N) 
y1 = np.random.rand(N)
y2 = np.random.rand(N)
y3 = np.pi * (15 * np.random.rand(N))**2 #0과 1 사이의 난수 30개를 생성 후 버블 크기 지정, 파이값을 곱하여 버블의 크기를 조절
plt.title("Bubble Chart")
plt.scatter(x, y1, c=y2, s=y3) #c: 버블색, s: 버블크기
plt.show()