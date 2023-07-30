students=[i for i in range(1,30+1)]

for j in range(28):
    submitnumber=int(input())
    students.remove(submitnumber)
students.sort()

for remainstudent in students:
    print(remainstudent)
