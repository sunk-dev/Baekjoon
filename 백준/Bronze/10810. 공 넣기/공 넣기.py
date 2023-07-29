backuts,chance=map(int,input().split())
backuts_list=[0]*backuts

for i in range (chance):
    start,end,ball_number=map(int,input().split())
    for j in range(start-1,end):
        backuts_list[j]=ball_number

for i in backuts_list:
    print(i,end=' ')