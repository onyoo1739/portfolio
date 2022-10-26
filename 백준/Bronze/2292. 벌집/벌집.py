N = int(input())
R = 1

while N > 1:
    N -= (6 * R)
    R += 1
print(R)
