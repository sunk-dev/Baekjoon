matrix=[[0] for _ in range(9)]

for l in range(9):
    low=list(map(int,input().split(' ')))
    matrix[l]=low

max=matrix[0][0]
low=0
colum=0
for l in range(9):
    for c in range(9):
        if matrix[l][c]>max:
            max=matrix[l][c]
            low=l
            colum=c

print(max)
print(f'{low+1} {colum+1}')