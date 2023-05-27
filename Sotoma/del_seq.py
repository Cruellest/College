def del_seq_f(seq,start,end):
    
    '''
        delete a sequence of positions in a array"
        @seq = the array
        @start = the first array to be deleted
        @end = the last position to be deleted
    '''
    if start == 0:
        lista = [None]*(len(seq)-(end-start))
    else:
        lista = [None]*(len(seq)-(end-start)-2)
    
    remover = [None]*(len(seq))
    
    for i in range(len(seq)):
        if i >= start and i < end:
            remover[i] = seq[i]
        
        elif i >= end:
            lista[i-end] = seq[i]
        
        else:
            lista[i] = seq[i]
    
    if type(seq) == list:
        return lista
            
    elif type(seq) == tuple:
        return tuple(lista)
            
    elif type(seq) == str:
        return "".join(lista)
