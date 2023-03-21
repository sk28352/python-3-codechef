t = int(input())
for i in range(t):
    N, M, K = map(int, input().split())
    if K*M>= N:
      print("Yes")
    else :
      print ("No")
