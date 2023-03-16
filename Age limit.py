t = int(input())           
for i in range(t):
    X, Y, A = map(int, input().split())
    if A>=X and A<Y:
     print("YES")
    elif A<X and A>Y:
     print("NO")
    else :
     print("NO")
