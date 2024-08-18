x = {"a": 10, "b": 20}
for k, v in x.items(): #딕셔너리 자료의 키와 값을 쌍으로 하여 반복하기위해 items 메서드 사용
    print("key [%s] => value [%d]" % (k, v))