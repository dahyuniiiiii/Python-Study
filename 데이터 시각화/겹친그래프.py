import matplotlib.pyplot as plt
plt.title("복수의 plot 명령을 한 그림에서 표현")
plt.plot([1, 4, 9, 16],c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5, mfc="r")
# c="b": 선색상 파란색
# lw=5: 선굵기는 5
# ls="--": 선스타일 점선(--)
# marker="o": 데이터 포인트를 동그라미(o)로 표시
# ms=15: 마커 크기 15
# mec="g": 마커 테두리 색 녹색
# mew=5: 마커 테두리 두께는 5
# mfc="r": 마커 내부 색상 빨간색
plt.plot([9, 16, 4, 1],c="k", lw=3, ls=":", marker="s", ms=10, mec="m", mew=5, mfc="c")
plt.show()