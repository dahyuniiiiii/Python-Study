# 시험 성적을 나타내는 임의의 숫자 5개를 리스트 변수 score에 넣고 평균 구하기
score = [40,80,90,40,60]
result = 0
for i in score:
    result += i
avg = result / len(score)
print(avg)