n=input()
a=list(n)
a.sort(reverse=True)
for i in range(len(a)):
    print(a[i], end='')