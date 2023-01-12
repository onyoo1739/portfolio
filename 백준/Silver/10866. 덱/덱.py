import sys
input=sys.stdin.readline
n=int(input())
s=[]
for i in range(n):
    a=input().split()
    o=a[0]
    if o=='push_front':
        s.insert(0,a[1])
    elif o=='push_back':
        s.append(a[1])
    elif o=='pop_front':
        if len(s)!=0:    
            print(s[0])
            del s[0]
        else:
            print(-1)
    elif o=='pop_back':
        if len(s)!=0:    
            print(s[-1])
            del s[-1]
        else:
            print(-1)
    elif o=='size':
        print(len(s))
    elif o=='empty':
        if len(s)==0:
            print(1)
        else:
            print(0)
    elif o=='front':
        if len(s)!=0:    
            print(s[0])
        else:
            print(-1)
    elif o=='back':
        if len(s)!=0:    
            print(s[-1])
        else:
            print(-1)