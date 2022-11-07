import sys
input=sys.stdin.readline

n=int(input())
b=[]
for i in range(n):
    b.append(int(input()))
c=sorted(b)
for i in c:
    print(i)