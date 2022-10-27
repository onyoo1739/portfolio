m=0

for i in range(9):
    a=list(map(int,input().split()))
    if max(a)>= m:
        m=max(a)
        x=i+1
        y=a.index(m)+1
print(m)
print(x,y)