import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

d1=dict()
for i in a:
    if d1.get(i)==None:
        d1[i]=1
    else:
        d1[i] +=1
for i in b:
    if d1.get(i) ==None:
        print(end='0 ')
    else:
        print(d1[i], end=' ')
