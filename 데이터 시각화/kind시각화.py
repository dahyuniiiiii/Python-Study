import seaborn as sns
import matplotlib.pylab as plt
iris = sns.load_dataset("iris")    #seaborn의 내장 데이터셋인 'iris'를 불러옴(붓꽃 데이터)
titanic = sns.load_dataset("titanic")    # 타이타닉호 데이터
iris.sepal_length[:20].plot(kind='bar', rot=0) #sepal_length: 꽃받침의 길이
#처음 20개의 값을 막대 그래프로 시각화, kind='bar': 막대 그래프, rot=0: x축 레이블의 회전 각도를 0도로 설정
plt.title("꽃받침의 길이 시각화")
plt.xlabel("Data")
plt.ylabel("꽃받침의 길이")
plt.show()
#<kind 대신 plot.bar>
# iris[:5].plot.bar(rot=0)
# plt.title("Iris 데이터의 Bar Plot")
# plt.xlabel("Data")
# plt.ylabel("각 Feature의 값")
# plt.ylim(0, 7)
# plt.show()