import sys
input=sys.stdin.readline
n=int(input())
b=[]
for i in range(n):
    b.append(input().strip())
set_b=set(b)
bb=list(set_b)
bb.sort()
bb.sort(key=len)
for j in bb:
    print(j)