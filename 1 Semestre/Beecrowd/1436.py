import math
rodadas = int(input())

for i in range(rodadas):
    a = input().split()
    
    for x in range(len(a)):
        a[x] = int(a[x])
        
    Pos = math.ceil(a[0]/2)
        
    print('Case {0}: {1}'.format(i+1,a[Pos]))