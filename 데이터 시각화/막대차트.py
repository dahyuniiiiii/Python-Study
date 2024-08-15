import matplotlib.pylab as plt #그래프나 차트를 그리기 위한 라이브러리
import numpy as np #수치 데이터를 쉽게 처리할 수 있게 도와주는 라이브러리
y = [2, 3, 1] #높이
x = np.arange(len(y)) #x위치를 위한 데이터 인덱스 생성
xlabel = ['가', '나', '다'] #x축 표시 레이블
plt.title("Bar Chart") #차트제목
plt.bar(x, y) #함수를 사용해 막대차트 생성
plt.xticks(x, xlabel) #x축 눈금 레이블 설정
plt.yticks(sorted(y)) #y축 눈금 레이블 설정
plt.xlabel("가나다") #x축이름
plt.ylabel("빈도 수") #y축이름
plt.show()
#범주형 데이터 크기비교(제품, 지역, 성별, 인구수, 설문, 매출)