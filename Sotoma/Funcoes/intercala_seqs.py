def intercala(seq1,seq2):
    
    '''
        append 2 arrays but every array 2 position will be igual to index(array1)+1
        @seq1 = array1
        @seq2 = array2
    '''
    
    array = [None]*(len(seq1)+len(seq2))
    
    cont = 0

    if len(seq1) == len(seq2):
        for i in range(len(seq1)):
            array[cont] = seq1[i]
            cont += 1
            array[cont] = seq2[i]
            cont += 1
    
    elif len(seq2) > len(seq1):
        for i in range(len(seq2)):
            if i > (len(seq1) - 1):
                array[cont] = seq2[i]
                cont += 1
            else:
                array[cont] = seq1[i]
                cont += 1
                array[cont] = seq2[i]
                cont += 1
                
    else:
        for i in range(len(seq1)):
            if i > (len(seq2) - 1):
                array[cont] = seq1[i]
                cont += 1
            else:
                array[cont] = seq1[i]
                cont += 1
                array[cont] = seq2[i]
                cont += 1
        
            
        
    return array