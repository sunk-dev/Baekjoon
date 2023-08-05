N,M=map(int,input().split())
a=[[0]*M for _ in range(N)] 
b=[[0]*M for _ in range(N)] 
a_plus_b=[[0]*M for _ in range(N)] 

행렬묶음=[a,b]
for i in range(2):
    for n in range(N):
        
        number_list=list(map(int,(input().split(' '))))
        행렬묶음[i][n]=number_list


for n in range(N):
    for m in range(M):
        a_plus_b[n][m]=a[n][m]+b[n][m]
for n in range(N):
    for m in range(M):
        print(a_plus_b[n][m],end=' ')
    print()