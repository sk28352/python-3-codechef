t = int(input())
for i in range(t):
    A,B,X = map(int,input().split())
    years = (B-A)//X
    print(years)
