from math import ceil

def fatia_seq_function(seq,start,end,step:int | None = 1):
    
    '''
        returns a slice of a array
        @seq = array
        @start = first part position of the sliced array
        @end = last position of the sliced array
        @step = the amount of steps of the sliced array
    '''
       
    cont = 0
    fatia = [None]*ceil((end-start)/step)
    for i in range(start,end,step):
        fatia[cont] = seq[i]
        cont += 1
    
    return fatia
