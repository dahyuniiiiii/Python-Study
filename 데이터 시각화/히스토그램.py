import matplotlib.pylab as plt 
import numpy as np
np.random.seed(0)
x = np.random.randn(1000) #난수 1000개 생성
plt.title("Histogram")
arrays, bins, patches = plt.hist(x, bins=10) #배열(구간에 포함된 데이터 개수, 구간 경계값, 막대들 정보)
#plt.hist()는 데이터 값의 범위와 빈도 보여줌, 데이터를 10개의 구간으로 나눔
plt.show()
print(repr(arrays)) #구간 별 데이터 개수
print(repr(bins)) #구간 경계값