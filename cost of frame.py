t = int(input())
for i in range(t):
    N, M, X = map(int, input().split())
    cost_of_frame = X*(2*(N+M))
    print(cost_of_frame)
