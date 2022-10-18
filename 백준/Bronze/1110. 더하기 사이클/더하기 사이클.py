n=int(input())
num=n
count=0
while 1:
    sum_num=(num//10)+(num%10)
    new_num=((num%10)*10) + (sum_num%10)
    count+=1
    if new_num ==n:
        break
    num=new_num
print(count)