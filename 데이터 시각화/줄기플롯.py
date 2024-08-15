import matplotlib.pylab as plt 
import numpy as np
x = np.linspace(0.1, 2 * np.pi, 10) #x값, 0.1에서 2π까지를 10개의 구간으로 균일하게 나눈 값
plt.title("Stem Plot")
plt.stem(x, np.cos(x), '-.') #np.cos(x)값의 줄기 플롯을 '-.' 스타일
plt.show()
#데이터가 시간이나 특정 순서에 따라 어떻게 변하는지 시각화할 때 유용 (신호 처리, 데이터 분석, 경제 데이터)