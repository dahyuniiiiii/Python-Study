import matplotlib.pylab as plt #차트 그리기를 위한 모듈
import numpy as np #수치 계산과 난수 생성
np.random.seed(0) #항상 동일한 난수 생성 - 시드값 설정

people = ['몽룡', '춘향', '방자', '향단'] 
y_pos = np.arange(len(people)) #y축에서 막대가 그려질 위치
performance = 3 + 10 * np.random.rand(len(people)) #3에서 13 사이의 값으로 각 사람의 성과를 랜덤하게 생성
error = np.random.rand(len(people)) #각 사람에 대한 오차 표시

plt.title("Barh Chart")
plt.barh(y_pos, performance, xerr=error, alpha=0.4) #y축 위치, 막대길이, 오차범위, 막대투명도(0이 투명)
plt.yticks(y_pos, people) #y축 눈금 설정
plt.xlabel('x 라벨') #x축 이름 설정
plt.show()
#데이터 비교 시 중첩(겹치거나 중복)