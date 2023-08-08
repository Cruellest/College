def mdc(v1,v2):
    r = None
    while True:
        if v1%v2 == 0:
            break
        
        else:    
            r = v1%v2
            v1 = v2
            v2 = r
            
    return v2

while True:
    try:
        entrada = input().split()
    
    except EOFError:
        break
    
    for i in range(2):
        entrada[i] = int(entrada[i])
        
    if entrada[0] == entrada[1]:
        print(4)
        
    else:
        perimetro = entrada[0] + entrada[1]   
        print((2*perimetro)//mdc(entrada[0],entrada[1]))        
