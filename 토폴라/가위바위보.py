import random as rd
li = ['r','p','c']
rs = 'y'

바위='r'
보='p'
가위='c'
def game() :
    c=0
    d=0
    while c<4 or d<3 :
        a=input('가위바위보 중 하나를 입력하시오.')
        c=c+1
        b = rd.choice(li)
        if b=='r' and a=='p' or b=='p' and a=='c' or b=='c' and a=='r' :
            d=d+1
            print('당신이 이겼습니다.')
            print('당신은 %d판 중 %d 판을 이겼습니다.' %(c,d))
        elif b==a :
            print('비겼습니다.')
            print('당신은 %d판 중 %d 판을 이겼습니다.' %(c,d))
        else :
            print('당신이 졌습니다.')
            print('당신은 %d판 중 %d 판을 이겼습니다.' %(c,d))
        if c==3:
            if d==1 or d==0:
                print('당신은 게임에서 졌습니다.')
            break
        if c==2 and d==0 :
            print('당신은 게임에서 졌습니다.')
        if c==3 and d==2 :
            print('당신은 게임에서 이겼습니다.')
            break
    return input('게임을 다시 하시겠습니까?(y/n)')


while  rs=='y' :
    rs=game() 

