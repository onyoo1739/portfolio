n=int(input())
a=list(map(int,input().split()))
sum=0

for h in range(n):
    sum=sum+(a[h]/max(a)*100)
print(sum/n)