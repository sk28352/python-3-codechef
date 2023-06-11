t = int(input())
for i in range(t):
    N, X, P = map(int,input().split())
    
    #n questions, x correct, p marks to pass
    total = (X*3 - (N-X))
    if total >= P:
        print("PASS")
    elif total < P:
        print("FAIL")
