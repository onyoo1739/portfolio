a=input()
al=['c=','c-','dz=','d-','lj','nj','s=','z=']
sum=0
for i in al:
    if i in a:
        sum+=a.count(i)
        a=a.replace(i,' ')
a=a.replace(' ',"")
sum+=len(a)
print(sum)
