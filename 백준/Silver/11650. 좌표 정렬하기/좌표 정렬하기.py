n=int(input())
a=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append([x,y])
a.sort()
for j in range(len(a)):
    print(str(a[j][0])+' '+str(a[j][1]))