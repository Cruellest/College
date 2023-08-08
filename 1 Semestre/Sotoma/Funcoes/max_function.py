def max_function(vet):
    
    '''
    Return the max value in an list, tuple or str
    '''
    
    max = vet[0]
    
    for i in range(len(vet)):
        if vet[i] > max:
            max = vet[i]
            
    return max
 