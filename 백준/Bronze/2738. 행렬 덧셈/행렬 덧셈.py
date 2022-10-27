n,m=map(int,input().split())
c=[]
d=[]

for i in range(n):
    a=list(map(int,input().split()))
    c.append(a)
for j in range(n):
    b=list(map(int,input().split())) 
    d.append(b)

for h in range(n):
    for q in range(m):
        print(c[h][q]+d[h][q],end=' ')
    print()
