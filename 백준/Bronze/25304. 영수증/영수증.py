X= int(input())
N= int(input())
rs=0
for i in range(N):
    a,b=map(int,input().split())
    rs += a*b
if rs==X:
    print('Yes')
else: 
    print('No')