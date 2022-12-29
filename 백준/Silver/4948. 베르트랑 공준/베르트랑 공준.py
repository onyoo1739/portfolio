import sys

input = sys.stdin.readline

inputList = list()

N = 123456*2 + 1
isPrime = [True] * N

for i in range(2, int(N**0.5)+1):
    if isPrime[i]:
        for j in range(2*i, N, i):
            isPrime[j] = False


def counting(inputValue):
    cnt = 0
    for k in range(inputValue+1, inputValue*2 + 1):
        if isPrime[k]:
            cnt += 1
    print(cnt)


while True:
    k = int(input())

    if not k:
        break
    counting(k)