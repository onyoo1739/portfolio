'''t1 = (1,2,3,4) 
t1 = (1,2)
t2 = (3,4)
print(t1)
3.
li=[(1,2), (3,4), (5,6)]

li[0]=list[li[0]]
li[0]=(7,8)
print(li)

4.
c=[]
for a in range(5):
    c.append(int(input('숫자?')))
print(set(c))

5.
t=(1,2,3,4)
t=list(t)
for a in range(4):
    t[a]= t[a]*10
t=tuple(t)
print(t)

1.
nums=[]
x=int(input('리스트길이'))
target=int(input('target = '))
for a in range(x):
    a=int(input('숫자를 입력하시오'))
    nums.append(a)
def g():
    for b in range(x-1):
        for c in range(x-1):
            if nums[b]+nums[c]==target:
                print([b,c])

                print(b,'번 숫자',nums[b],'와', c,'번 숫자 ',nums[c],'를 더하여' ,target,'이 됩니다. 따라서 답은 ',[b,c],'입니다.')
                return True
    
    print('답이 없습니다.')
g()

2.
nums=[]
d=[]
x=int(input('리스트길이'))
for a in range(x):
    a=int(input('숫자를 입력하시오'))
    nums.append(a)
for b in range(x-1):
    for c in range(b+1,x-1):
        d.append(nums[b]+nums[c]
                     
print(set(d))

3.
a,b= map(int,input('숫자를 입력하시오.').split(","))

m = min(a,b)
while True:
    m-=1
    if a%m==0 and b%m==0:
        break
print(m)
n = max(a,b)
while True:
    if n %a ==0 and n%b==0:
        break
    n+=1
print(n)
print(m)
d=list(n,m)
print(c)

4.
N=int(input('숫자를 입력하시오.'))
def get_primenum(N):
    for a in range (2,N):
        if N%a==0:
            return False
    return True

print(get_primenum(N))

5.
c=1
n= int(input(' 숫자를 입력합니다.'))
for a in range(1,n+1):
    c = c*a
print(c)
'''
6.

a= int(input('숫자를 입력하시오'))
b=list(str(a))
c=0
5,6
for d in (b):
    d= int(d)
    c+=d
print(c)
'''
7.
N=int(input('숫자를 입력하시오'))
x=1
while x<=1000:
    if N%x == 0:
          x=x+N
          print(x)'''
