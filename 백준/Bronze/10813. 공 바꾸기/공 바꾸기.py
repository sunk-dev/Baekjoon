backuts,chance=map(int,input().split())
backuts_list=[x for x in range(1,backuts+1)]


for i in range (chance):
    change_b1,change_b2=map(int,input().split())
    backuts_list[change_b1-1],backuts_list[change_b2-1]=backuts_list[change_b2-1],backuts_list[change_b1-1]

for i in backuts_list:
    print(i,end=' ')