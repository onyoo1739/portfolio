a=[]
for i in range(5):
    n=int(input())
    a.append(n)
    a.sort()
print(int(sum(a)/5))
print(a[(len(a)//2)])