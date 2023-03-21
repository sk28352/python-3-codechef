t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    
    if (X*100) == (Y*10):
        print("Cloth")
    elif (X*100) < (Y*10):
        print("Disposable")
    elif (X*100) > (Y*10):
       print("Cloth")
