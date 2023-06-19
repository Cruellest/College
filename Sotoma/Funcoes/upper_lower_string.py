def upper_string_pt(st):
    
    '''
    converts a upperletter str to a lowerletter version of itself
    '''
    
    st = list(st)
    
    for i in range(len(st)):
        
        if int(ord(st[i])) >= 65 and int(ord(st[i]) <=90):
            st[i] = chr(ord(st[i])+32)
        
    st = "".join(st)
    return st

def lower_string_pt(st):
    
    '''
    converts a lowerletter str to a upperletter version of itself
    '''
    
    st = list(st)
    
    for i in range(len(st)):
        
        if int(ord(st[i])) >= 97 and int(ord(st[i]) <=122):
            st[i] = chr(ord(st[i])-32)
        
    st = "".join(st)
    return st
