t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    
    weekend = [6,7,13,14,20,21,27,28]
    total = A + weekend
    total_unique = list(set(total))
    print(len(total_unique))
        
