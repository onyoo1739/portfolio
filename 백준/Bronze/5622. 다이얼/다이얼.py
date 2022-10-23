s=input()
li=['ABC','DEF','HIG','JKL','MNO','PQRS','TUV','WXYZ']
time=0
for i in s:
    for h in li:
        for j in h:
            if i==j:
                time+=li.index(h)+3
print(time)