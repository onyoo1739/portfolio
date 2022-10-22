a= input().upper()
w_l=list(set(a))
c_l=[]
for i in w_l:
    cnt=a.count(i)
    c_l.append(cnt)
if c_l.count(max(c_l))>1:
    print('?')
else:
    max_index=c_l.index(max(c_l))
    print(w_l[max_index])