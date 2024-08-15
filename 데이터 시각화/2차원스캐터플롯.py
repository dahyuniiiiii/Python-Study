import matplotlib.pylab as plt
import numpy as np
np.random.seed(0)
#평균이 0, 표준편차가 1인 정규 분포를 따르는 난수 100개 생성
#np.random.normal은 정규 분포를 따르는 난수를 생성하는 데 사용
X = np.random.normal(0, 1, 100)
Y = np.random.normal(0, 1, 100)
plt.title("Scatter Plot")
plt.scatter(X, Y) #산점도로 표시
plt.show()
#두 변수 간의 관계를 시각적으로 확인하는 데 유용