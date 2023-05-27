def append_lst_function(lst,val):
    
    '''
    Return a version of a array with a new item in the last position
    '''
    
    append = [None]*(len(lst)+1)
    for i in range(len(lst)):
        append[i] = lst[i]
    
    append[len(lst)] = val
    
    return append
