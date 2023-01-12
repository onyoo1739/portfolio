from sys import stdin

stk1 = list(stdin.readline().strip())
stk2 = []
n = int(input())

for _ in range(n):
    comm = stdin.readline().strip()

    if comm == 'L':
        if stk1 != []:
            stk2.append(stk1.pop(-1))
    elif comm == 'D':
        if stk2 != []:
            stk1.append(stk2.pop(-1))
    elif comm =='B':
        if stk1 != []:
            stk1.pop(-1)
    elif 'P' in comm:
        stk1.append(comm[2])

print(''.join(stk1+list(reversed(stk2))))

