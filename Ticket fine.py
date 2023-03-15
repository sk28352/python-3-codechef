t = int(input())
for i in range(t):
    X, P, Q = map(int,input().split())
    if Q == P:
        total_fine = X*0
        print(total_fine)
    if Q < P:
        total_fine = X*(P-Q)
        print(total_fine)
