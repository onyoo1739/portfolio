n=int(input())
h=0
for a in range(1,n+1):
    if a<=99:
        h+=1
    else:
        ns=list(map(int,str(a)))
        if ns[0]-ns[1] == ns[1]-ns[2]:
            h+=1
print(h)        