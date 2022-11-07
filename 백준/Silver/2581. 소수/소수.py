m=int(input())
n=int(input())
a=[]
for i in range(m,n+1):
    n=0
    for j in range(2,i):
        if i%j==0:
            n+=1        
            break
    if n==0 and i !=1:
        a.append(i)
if a==[]:
    print(-1)
else:
    print(sum(a))
    print(min(a))
