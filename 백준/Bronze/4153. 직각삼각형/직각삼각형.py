while True:
    a,b,c=map(int,input().split())
    if a==b==c==0:
        break
    d=[a,b,c]
    M=max(d)
    d.remove(M)
    if M**2==d[0]**2+d[1]**2:
        print('right')
    else:
        print('wrong')