n,m=map(int,input().split())
li=list(map(int,input().split()))
a=[]
for i in range(n):
    for j in range(i,n):
        for h in range(j,n):
            if i!= j!= h:
                a.append((li[i]+li[j]+li[h]))
a=set(a)
a=list(a)
for i in a[:]:
    if i>m:
        a.remove(i)
print(max(a))
