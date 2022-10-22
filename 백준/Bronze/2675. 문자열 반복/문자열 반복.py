t=int(input())
for i in range(t):
    n,s= input().split()
    text=''
    for i in s:
        text +=int(n)*i
    print(text)