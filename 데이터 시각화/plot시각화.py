import pandas as pd #데이터분석
import numpy as np #수치계산
import matplotlib.pylab as plt #데이터시각화
np.random.seed(0)
df1 = pd.DataFrame(np.random.randn(100, 3), index=pd.date_range('1/1/2018', periods=100), columns=['A', 'B', 'C']).cumsum()
#100개의 행과 3개의 열, 2018년 1월 1일부터 100일 동안의 날짜 인덱스를 생성, 데이터를 누적 합으로 변환
print(df1.tail()) #DataFrame의 마지막 5개의 행을 출력
df1.plot()
plt.title("Pandas의 Plot메소드 사용 예")
plt.xlabel("시간")
plt.ylabel("Data")
plt.show()
