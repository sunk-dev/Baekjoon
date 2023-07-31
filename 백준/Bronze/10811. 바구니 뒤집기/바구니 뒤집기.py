bucket,chance=map(int,input().split(' '))
buckets=[x for x in range(1,bucket+1)]

for i in range(chance):
    first,end=map(int,input().split(' '))
    buckets[first-1:end]=reversed(buckets[first-1:end])

for b in buckets:
    print(b,end=' ')