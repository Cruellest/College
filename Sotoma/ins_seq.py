def ins_seq_f(seq,pos,val):
    
    '''
        inserts a value in a index of an array
        @seq = the array
        @pos = the index that the value will be placed
        @val = the value
    '''
    
    lista = [None]*(len(seq)+1)
    
    for i in range(len(lista)):
        if i == pos:
            lista[i] = val
            for j in range(i+1,len(lista)):
                lista[j] = seq[j-1]

            if type(seq) == list:
                return lista
            
            elif type(seq) == tuple:
                return tuple(lista)
            
            elif type(seq) == str:
                return "".join(lista)
        
        else:
            lista[i] = seq[i]