standard_input = ["098.447.895-55","733.184.680-96"]

while True:
    try:
        cpfin = input().split(".")
    
    except EOFError:
        break
    
    cpfin = "".join(cpfin)
    cpfin = cpfin.split("-")
    cpfin = "".join(cpfin)
    cpfin = list(cpfin)
    
    for i in range(11):
        cpfin[i] = int(cpfin[i])
   
    #auth dig1
    authdig1 = 0
    process1 = 0
    for x in range(1,10):
        process1 = process1 + (cpfin[x-1]*(x))
    
    if process1%11 == 10:
        authdig1 = 0
    else:
        authdig1 = process1%11
        
    #auth dig2
    authdig2 = 0
    process2 = 0
    cont = 0
    for j in range(9,0,-1):
        process2 = process2 + (cpfin[cont]*(j))
        cont += 1
        
    if process2%11 == 10:
        authdig2 = 0
    else:
        authdig2 = process2%11
    
    if cpfin[9] == authdig1 and cpfin[10] == authdig2:
        print("CPF valido")
    
    else:
        print("CPF invalido")