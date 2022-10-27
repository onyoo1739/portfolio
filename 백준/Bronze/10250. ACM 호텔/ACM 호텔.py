t=int(input())
for i in range(t):
    w,h,n=map(int,input().split())
    if n%w==0:
        print(w*100 + (n//w))
    else:
        print((n%w)*100 + (n//w+1))
