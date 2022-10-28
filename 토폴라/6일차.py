'''1.
a=int(input('수를 입력하시오'))
li=[]
for b in range(a):
    li2=[]
    for c  in range (b+1):
        li2.append(c+1)
    li.append(li2)
    
print(li)'''

3.
'''
li=[]

for a in range (5):
    li2=[]
    for b in range(1,6):
        li2.append(a*5 + b)
    li.append(li2)
print(li)

li = [6,1,7,8,5,3,5,7,8,3]#오름차순
for d in range(10) :
    min_li = d
    for c in range(d,10):
        if li[min_li]> li[c]:
            min_li = c
    li[d],li[min_li] = li[min_li],li[d] 
print(li)'''

4.
import random as rd
e=[]
g=0
for a in range(6):
    b=[]
    for c in range (6):
        m = rd.randint(0,1)
        b.append(m)
    e.append(b)
print(e)
for h in range(6):
    g+= e[h].count(1)
print(g)
