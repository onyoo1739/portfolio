import random as rd
n= rd.randint(1,100)
rs = 'y'
while rs=='y':
    import random as rd
    n= rd.randint(1,100)
    for b in range (1,11):
        a=int(input('숫자를 입력 하세요 :'))
        if n>a :
          print( '%d번 시도, 이 숫자보다 큽니다.' %b)
        elif n==a :
            print('게임에서 이겼습니다.')
            rs=input('게임을 재시작 하겠습니까? (y/N)')
            break
        else :
            print('%d번 시도, 이 숫자보다 작습니다.' %b)
        if b==10 :
            print('10번의 기회를 모두 사용하였습니다.'
                     '게임에서 졌습니다.')
            res=input('게임을 재시작 하겠습니까? (y/N)')
print("게임을 종료합니다.")


'''
while n<9 :
    n=n+1
    for a in range (1,10) :
        print( n, 'x', a, '=', n*a)
 '''
