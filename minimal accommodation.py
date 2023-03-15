t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    cost = min(3*X,2*Y)
    print(cost)
