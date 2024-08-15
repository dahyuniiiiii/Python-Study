import seaborn as sns
#데이터셋 종류: iris, tips, penguins, diamonds, flights, titanic
import matplotlib.pylab as plt
titanic = sns.load_dataset("titanic")
df3 = titanic.pclass.value_counts()
df3.plot.pie(autopct='%.2f%%') #각 조각의 비율을 소수점 두 자리까지 표시 후 %붙임
plt.title("선실별 승객 수 비율")
plt.axis('equal') #정확한 원형으로 설정
plt.show()

# iris = sns.load_dataset("iris")
# iris.plot.hist() #히스토그램
# plt.title("각 Feature 값들의 빈도수 Histogram")
# plt.xlabel("데이터 값")
# plt.show()

# iris = sns.load_dataset("iris")
# iris.plot.kde() #Kernel Density Plot
# plt.title("각 Feature 값들의 빈도수에 대한 Kernel Density Plot")
# plt.xlabel("데이터 값")
# plt.show()

# iris = sns.load_dataset("iris")
# iris.plot.box() #Box Plot
# plt.title("각 Feature 값들의 빈도수에 대한 Box Plot")
# plt.xlabel("Feature")
# plt.ylabel("데이터 값")
# plt.show()