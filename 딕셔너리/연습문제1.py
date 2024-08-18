data = {
    "철수": 98,
    "영희": 80,
    "순이": 100,
    "돌이": 70,
}
for a,b in data.items():
    print(a,'    ',b)
print('='*20)
total = 0 #sum은 파이썬 내장함수라 변수명x
for b in data.values():
    total += b
avg = total/len(data)
print('평균','   ',int(avg))