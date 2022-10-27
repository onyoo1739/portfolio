x=int(input())
n=0
n_count=0
while n_count <x:
    n+=1
    n_count+=n
n_count-=n

if n%2 ==0:
    i=x-n_count
    j=n-i+1
else:
    i=n-(x-n_count)+1
    j=x-n_count
print(f"{i}/{j}")
    