t = int(input())
for i in range(t):
    N, M = map(int, input().split())
    if N<= M:
        print(N)
    elif N>M:
        print(2*N-M)
