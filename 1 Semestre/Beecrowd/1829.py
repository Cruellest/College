rounds = int(input())
PedroPoints = 0
LucasPoints = 0
roundsT = 0
R = [None]*rounds

for i in range(rounds):
    LucasIn = input().split("^")
    
    for n in range(2):
        LucasIn[n] = int(LucasIn[n])
        
    LucasV = LucasIn[0]**LucasIn[1]
    
    PedroIn = input().split("!")
    PedroIn = int(PedroIn[0])
    
    for x in range(PedroIn,1,-1):
        PedroIn *= (x-1)
        
    if PedroIn > LucasV:
        PedroPoints += 1
        R[i] = 1
    else:
        LucasPoints += 1
        R[i] = 2
        
if PedroPoints == LucasPoints:
        print("A competicao terminou empatada!")
    
elif PedroPoints > LucasPoints:
        print("Campeao: Pedro!")
        
else:
        print("Campeao: Lucas!")

for m in range(rounds):
    if R[m] == 1:
        print("Rodada #{0}: Pedro foi o vencedor".format(m+1))
    elif R[m] == 2:
        print("Rodada #{0}: Lucas foi o vencedor".format(m+1))