students = ['가','나','다','라','마','바','사','아','자','차'] #10명으로 이루어진 반의 학생 이름
students.append('카') #전학생 이름 추가
print(students)
del students[0] #전학 간 학생 이름 삭제
print(students)
print(students[4:9]) #슬라이싱으로 5번~9번 학생 새로운 리스트
