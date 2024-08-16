import matplotlib.pylab as plt
import numpy as np
np.random.seed(0)
#np.random.normal은 numpy 라이브러리의 함수로, 정규분포에서 무작위 데이터를 생성
X = np.random.normal(0, 1, 100) #평균이 0, 표준편차가 1인 정규분포에서 100개의 값을 랜덤으로 생성하여 X에 저장
Y = np.random.normal(0, 1, 100)
plt.title("Scatter Plot")
plt.scatter(X, Y) #산점도로 표시
plt.show()
#두 변수 간의 관계를 시각적으로 확인하는 데 유용