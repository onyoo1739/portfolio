n=int(input())
a=[[0]*100 for _ in range(100)]
for _ in range(n):
    x,y=map(int,input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            a[i][j]=1
count=0
for i in range(100):
    for j in range(100):
        if a[i][j] ==1:
            count+=1
print(count)