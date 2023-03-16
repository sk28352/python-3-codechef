t = int(input())
for i in range(t):
    X, Y, Z = map(int, input().split())
    if X>Y and X>Z:
        print("Setter")
    elif Y>X and Y>Z:
        print("Tester")
    else:
        print("Editorialist") 
