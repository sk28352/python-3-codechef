t = int(input())           
for i in range(t):
    #Accept 4 integers as input
    X1,Y1,X2,Y2 = map(int, input().split()) 
    style_1 = X1+Y1
    style_2 = X2+Y2
    
    if (style_1)>(style_2):
        print(style_2)
        
    elif (style_1)<(style_2):
        print(style_1)
