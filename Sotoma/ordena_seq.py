def ordena(seq,crescente:bool | None = True):

    '''
        it sorts a array using the insertion sort method
        @seq = the array
        @crescente = it is a boolean if it is True the sort will be crescent if False
        it will be decreasing
    '''
    
    
    if crescente == True:
        for i in range(1,len(seq)):
            number = seq[i]
            x = i-1
            
            while (x) >=0 and number < seq[x]:
                seq[x+1] = seq[x]
                x -= 1
                seq[x+1] = number
    
    else:
        for i in range(1,len(seq)):
            number = seq[i]
            x = i-1
            
            while (x) >=(0) and number > seq[x]:
                seq[x+1] = seq[x]
                x -=1
                seq[x+1] = number



    return seq
