# -*- coding: utf-8 -*-

standard_input = ["2","1 3 2 5 7 9 4 6 8","4 9 8 2 6 1 3 7 5","7 5 6 3 8 4 2 1 9","6 4 3 1 5 8 7 9 2","5 2 1 7 9 3 8 4 6","9 8 7 4 2 6 5 3 1","2 1 4 9 3 5 6 8 7","3 6 5 8 1 7 9 2 4","8 7 9 6 4 2 1 5 3","1 3 2 5 7 9 4 6 8","4 9 8 2 6 1 3 7 5","7 5 6 3 8 4 2 1 9","6 4 3 1 5 8 7 9 2","5 2 1 7 9 3 8 4 6","9 8 7 4 2 6 5 3 1","2 1 4 9 3 5 6 8 7","3 6 5 8 1 7 9 2 4","8 7 9 6 4 2 1 3 5"]

Rounds = int(input())

for i in range(Rounds):
    
    Checkmate = True
    Matriz = [input().split()]
    
    
    for j in range(len(Matriz)):
        Matriz[0][j] = int(Matriz[0][j])
        
    for x in range(9):
        if x <8:
            Matriz.append(input().split())
        for k in range(9):
            Matriz[x][k] = int(Matriz[x][k])
    
    MatrizMine = [[0]*9]
    for m in range(8):
        MatrizMine.append([0]*9)
    Bloco = 0
    cont = [0]*3
    for g in range(9):
        if g == 3:
            Bloco = 3
            cont =[0]*3
        elif g == 6:
            Bloco = 6
            cont = [0]*3
        
        for h in range(9):
            if h > 2 and h < 6:
                MatrizMine[Bloco+1][cont[1]] = Matriz[g][h]
                cont[1] += 1
            elif h > 5:
                MatrizMine[Bloco+2][cont[2]] = Matriz[g][h]
                cont[2] +=1
            
            else:
                MatrizMine[Bloco+0][cont[0]] = Matriz[g][h]
                cont[0] += 1 
        
    

    for c in range(9):
        CheckerMinecraft = [0]*9
        Checker = [0]*9
        CheckerVert = [0]*9
        for a in range(9):
            Checker[(Matriz[c][a])-1] += 1
            CheckerMinecraft[(MatrizMine[c][a])-1] += 1
            CheckerVert[(Matriz[a][c])-1] += 1
            if Checker[(Matriz[c][a]) -1] > 1 or CheckerMinecraft[(MatrizMine[c][a])-1] > 1 or CheckerVert[(Matriz[a][c])-1] > 1:
                Checkmate = False
                break
    
    

        
            
    print("Instancia {0}".format(i+1))
    
    if Checkmate == True:
        print("SIM")
        print()
    else:
        print("NAO")
        print()