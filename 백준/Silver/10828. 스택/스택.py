import sys
input=sys.stdin.readline
n=int(input())
s=[]
for i in range(n):
    a=input().split()
    o=a[0]
    if o=='pop':
        if len(s)!=0:
            print(s[-1])
            del s[-1]
        else:
            print(-1)
    elif o=='size':
        print(len(s))
    elif o=='empty':
        if len(s)!=0:
            print(0)
        else:
            print(1)
    elif o=='top':
        if len(s)==0:
            print(-1)
        else:
            print(s[-1])
    elif o=='push':
        s.append(int(a[1]))