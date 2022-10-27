n=int(input())
start=n//5
output=-1
for a in range(start,-1,-1):
    if (n-5*a)%3 ==0:
        output = a+(n-5*a)//3
        break
print(output)