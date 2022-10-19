import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    score=0
    con=0
    ox=list(input())
    for i in ox:
        if i=='O':
            con+=1
            score+=con
        else:
            con=0
    print(score)