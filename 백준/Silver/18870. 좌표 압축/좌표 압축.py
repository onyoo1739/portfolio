n=int(input())
nlist=list(map(int,input().split()))
nlist2=list(sorted(set(nlist)))
dic={value:index for index, value in enumerate(nlist2)}
for i in nlist:
    print(dic[i], end=' ')
#규칙 -> 오름차순 후 해당하는 인덱스의 값을 프린트하는 것