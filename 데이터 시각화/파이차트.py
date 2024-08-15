import matplotlib.pylab as plt 
from matplotlib import font_manager, rc #시스템 폰트 관리 및 matplotlib의 특정 폰트 변경

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 폰트 파일 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


labels = ['개구리', '돼지', '개', '통나무'] #항목
sizes = [15, 30, 45, 10] #비율
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'] #색상
explode = (0, 0.1, 0, 0) #강조할 부분+약간 분리
plt.title("Pie Chart")
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90) #파이조각비율, 그림자추가, 90도시작으로 시계반대방향으로 파이조각 그림
plt.axis('equal') #차트를 정확한 원형으로 표시
plt.show()