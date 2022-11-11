import sys
input=sys.stdin.readline
n=int(input())
a=[]
for i in range(n):
    y,x=map(int,input().split())
    a.append([x,y])
b=sorted(a)
for j in range(n):
    print(b[j][1],b[j][0])