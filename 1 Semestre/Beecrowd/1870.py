standard_input = ["4 7 6","3 0 0 0 0 0 5",'2 0 0 0 0 0 4','1 0 1 0 0 0 1','1 0 1 0 0 0 1','3 0 0 0 1 0 1','0 0 0']


Info = [None]*3
while True:
    
    Info = input().split()
    for cu in range(3):
        Info[cu] = int(Info[cu])
    if Info[0] == 0 and Info[1] == 0 and Info[2] == 0:
        break
        
    Matriz = [input().split()]
    for x in range(Info[0]):
        Matriz.append(input().split())
        
        