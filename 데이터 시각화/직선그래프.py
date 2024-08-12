# 터미널에 pip install matplotlib 입력하여 설치
import matplotlib.pyplot as plt
plt.title("Plot") #제목
plt.xlabel("X") #엑스축 제목
plt.ylabel("Y") #와이축 제목
#plt.plot([1,4,9,16]) #y값, x값은 자동으로[0,1,2,3]설정
#plt.plot([10, 20, 30, 40], [1, 4, 9, 16], 'rs--') #앞은 x값 뒤는 y값 #rs는 실선
plt.plot([10, 20, 30, 40], [1, 4, 9, 16], c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5, mfc="r")
#색깔 지정시 약자 사용 ,lw : 선굵기 ,ls : 선스타일,marker : 마커종류, ms : 마커크기, mec : 마커선색깔, mew : 마커선굵기, mfc : 마커내부색
plt.xlim(0, 50) #x축 범위 수동 지정
plt.ylim(-10, 30) #y축 범위 수동 지정
plt.show()