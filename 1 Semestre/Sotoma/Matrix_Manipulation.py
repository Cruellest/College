def conv_MatrixType(Matrix,ty):
    
    '''
    This is a code that converts all the elements of a matrix to the same 
    type of element
    @Matrix = The matrix to be converted
    @ty = the type that the elements will be converted
    '''
    
    if ty == float:
        for j in range(len(Matrix)):
            for x in range(len(Matrix[j])):
                Matrix[j][x] = float(Matrix[j][x])
    
    if ty == int:
        for j in range(len(Matrix)):
            for x in range(len(Matrix[j])):
                Matrix[j][x] = int(Matrix[j][x])
    
    if ty == str:
        for j in range(len(Matrix)):
            for x in range(len(Matrix[j])):
                Matrix[j][x] = str(Matrix[j][x])
    
    return Matrix

def conv_MatrixPortionstoLinear(Matrix):
    import math
    holder = 0
    kid = math.sqrt(len(Matrix[0]))
    cont = [0]*(kid)
    times = 1
    for g in range(len(Matrix)):
        if g == (kid*times) and g != (len(Matrix)-1):
            holder = g - 1
            cont = [0]*kid
            times += 1
        for h in range(Matrix[g]):
            if
    



standard_input = ["1 3 2 5 7 9 4 6 8","4 9 8 2 6 1 3 7 5","7 5 6 3 8 4 2 1 9","6 4 3 1 5 8 7 9 2","5 2 1 7 9 3 8 4 6","9 8 7 4 2 6 5 3 1","2 1 4 9 3 5 6 8 7","3 6 5 8 1 7 9 2 4","8 7 9 6 4 2 1 5 3","1 3 2 5 7 9 4 6 8","4 9 8 2 6 1 3 7 5","7 5 6 3 8 4 2 1 9","6 4 3 1 5 8 7 9 2","5 2 1 7 9 3 8 4 6","9 8 7 4 2 6 5 3 1","2 1 4 9 3 5 6 8 7","3 6 5 8 1 7 9 2 4","8 7 9 6 4 2 1 3 5"]


Matriz = [input().split()]
for x in range(18):
        if x <17:
            Matriz.append(input().split())
            
conv_MatrixType(Matriz,float)
