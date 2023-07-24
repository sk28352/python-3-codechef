t = int(input())
for i in range(t):
    S = input()
    T = input()
    
    M = ""
    i = 0
    while i<len(S):
        
        if S[i]== T[i]:
            M = M +'G'
        
        else:
            M = M + 'B'
        i = i+1 
    print(M)
