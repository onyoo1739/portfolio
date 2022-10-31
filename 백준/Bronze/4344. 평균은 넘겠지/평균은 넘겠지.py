c=int(input())
for i in range(c):
    n=list(map(int,input().split()))
    cnt=0
    for h in n[1:]:
        mid=sum(n[1:])/n[0]
        if h>mid:
            cnt+=1
    v=cnt/n[0]*100
    print(f'{v:.3f}%')