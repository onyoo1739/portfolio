def self(n):
    a=list(str(n))
    res=n
    for i in range(len(a)):
        res+=int(a[i])
    return res
        
nums=[]
for i in range(1,10001):
    nums.append(self(i))
    if i not in nums:
        print(i)