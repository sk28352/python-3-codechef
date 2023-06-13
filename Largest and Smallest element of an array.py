t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int,input().split()))
    
    small = A[0]
    large = A[0]
    
    i = 0
    while i < len(A):
        if A[i] > large:
            large = A[i]
        
        if A[i] < small:
            small = A[i]
        i = i+1 
        
    print(small, large)
