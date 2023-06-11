t = int(input())
for i in range(t):
    K, X = map(int, input().split())
    time = ((K*7) - X)
    print(time)
