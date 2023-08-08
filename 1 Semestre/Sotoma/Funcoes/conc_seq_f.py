def conc_seq_function(vet1,vet2):

    '''
        return the concatenation of 2 arrays or strings
        @vet1 = array 1
        @vet2 = array 2
        @conc = concatenation of both arrays
    '''
    
    conc = [None]*(len(vet1)+len(vet2))
    
    for i in range(len(vet1)+len(vet2)):
        if i <= (len(vet1)-1):
            conc[i] = vet1[i]
        
        else:
            conc[i] = vet2[i - len(vet1)]
            
    if type(vet1) == str:
        conc = "".join(conc)
    
    elif type(vet1) == tuple:
        conc = tuple(conc)
    
    return conc