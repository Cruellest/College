def prox_val(seq,i):
    
    '''
        return the value of the next index in the array
        @seq = array name
        @i = selected array index
    '''
    
    if i == (len(seq)-1):
            return seq[0]
    
    else:
        return seq[i+1]