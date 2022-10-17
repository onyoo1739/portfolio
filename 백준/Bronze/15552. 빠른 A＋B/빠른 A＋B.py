import sys

read = lambda:sys.stdin.readline().rstrip()
T=int(read())

for i in range(T):
    a,b=map(int,read().split())
    
    print(a+b)