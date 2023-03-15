t =int(input())
for i in range(t):
    
    a,b=map(int,input().split())
    if a>b:
        print(7-a)
    elif b>=a:
        print(7-b)
        
