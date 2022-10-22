s=input()
li=list(s)
A='abcdefghijklmnopqrstuvwxyz'
for i in A:
    if i in s:
        print(s.index(i))
    else :
        print(-1)