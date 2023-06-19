for _ in range(int(input())):
    d,l,r=map(int,input().split())
    if d in range(l,r+1):
        print("Take second dose now")
    elif d>r:
        print("Too Late")
    else:
        print("Too Early")
