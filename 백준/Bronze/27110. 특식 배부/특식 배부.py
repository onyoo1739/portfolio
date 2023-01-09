n=int(input())
a,b,c=map(int,input().split())
cnt=0
if n-a>0:
    cnt+=a
else:
    cnt+=n
if n-b>0:
    cnt+=b
else:
    cnt+=n
if n-c>0:
    cnt+=c
else:
    cnt+=n
print(cnt)