x,y,w,h=map(int,input().split())
a=[]
a.append(x-0)
a.append(y-0)
a.append(w-x)
a.append(h-y)
print(min(a))