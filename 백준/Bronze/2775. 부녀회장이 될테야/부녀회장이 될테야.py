t=int(input())
for j in range(t):
    k=int(input())
    n=int(input())
    zero=[i for i in range(1,n+1)]
    for p in range(k):
        for m in range(1,n):
            zero[m]+=zero[m-1]
    print(zero[-1])