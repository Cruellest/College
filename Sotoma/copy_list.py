def copy_list(vet):
    
    '''
        Copy a list to another memory adress
    '''
    
    b = [None]*(len(vet))
    
    for i in range(len(vet)):
        b[i] = vet[i]
        
    return b