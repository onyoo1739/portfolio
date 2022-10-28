re=''
n=''
f,g=0,0
running = True
rs='y'

def game():
    player='x'
    print('=========틱택토 게임을 시작합니다.')
    print("=========플레이어 1과 플레이어 2가 번갈아가며 'X'와 'O'를 플레이하게 됩니다.")
    print('=========자기 차례에 행,열에 해당되는 숫자 2개를 1,1 처럼입력해 주세요 (1열 1행)')
    e=[[1,1,1],[1,1,1], [1,1,1]]
    while running :
        while re==n :
            #li = list(map(int,(input().split(","))))
            a,b = map(int,input("player "+player+" turn : ").split(","))
            #a = int(input('플레이어'+player+'의 차례 :'))
            #b=int(input('플레이어'+ player+ '의 차례 :'))
            if not (a in [1,2,3] and b in [1,2,3]) :
                print('다시 입력하시오')
                re==n
            elif e[a-1][b-1]!=1 :
                print('이미 플레이된 위치입니다. 다른 위치에 놓아주세요.')
                re==n
            else :
                break
        print('플레이어'+player+'이 %d행 %d열에 플레이 했습니다.' %(a,b))
        print('결과')
        e[a-1][b-1] = player
        for i in e:
            print(i)
        for k  in range(3):
            if e[k][0]==e[k][1]==e[k][2] !=1 or e[0][k]==e[1][k]==e[2][k] !=1  :
                print(player+'플레이어의 승리입니다.')
                return input('게임을 다시 하시겠습니까?(y/n)')
        if e[0][0]==e[2][2]==e[1][1] !=1 or e[0][2]==e[1][1]==e[2][0] !=1 :
            print(player+'플레이어의 승리입니다.')
            return input('게임을 다시 하시겠습니까?(y/n)')

        if  not (1 in e[1] or 1 in e[0] or 1 in e[2]):
            print('더이상 공간이 없습니다. 무승부입니다.')
            break
        if player =='x':
            player ='o'
        else:
            player = 'x'
        



while rs=='y':
    game()
