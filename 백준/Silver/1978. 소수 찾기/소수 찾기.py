n=int(input())
cnt=0
a=list(map(int,input().split()))
for h in a:
    for j in range(2,h+1):
        if h%j==0:
            if j==h:
                cnt+=1
            break
print(cnt)
            
    