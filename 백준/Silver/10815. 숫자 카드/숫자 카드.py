n=int(input())
a=set(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
for h in b:
    if h in a:
        print(1, end=' ')
    else:
        print(0, end=' ')
