x = {"a": 10, "b": 20}
print(len(x)) #자료 개수
print(x["a"]) #value값 확인
x["a"]=30 #자료 갱신
print(x) 
x["c"]=40 #자료 추가
print(x)
del x["b"] #자료 삭제
print(x)
print("a" in x) #키 확인
