t = int(input())
for i in range(t):
    X, Y = map(int,input().split())
    
    count = X//Y        
    people = count//2
    print(people)
