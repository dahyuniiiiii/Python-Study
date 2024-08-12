import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0., 5., 0.2) #0.=0.0 #0부터 5까지 0.2 간격으로 값 생성
plt.title("라인 플롯에서 여러개의 선 그리기")
plt.plot(t, t, 'r--', t, 0.5 * t**2, 'bs:', t, 0.2 * t**3, 'g^-') #빨간색 대시선, 파란색 점선, 초록색 삼각형 마커 선
plt.show()