rounds = int(input())

for i in range(rounds):
    Letras = [0]*26
    Phrasis = input().split()
    Phrasis = "".join(Phrasis)
    Phrasis = list(Phrasis)
    
    for x in range(len(Phrasis)):
        if ord(Phrasis[x]) <= 122 and ord(Phrasis[x]) >=97:
            Letras[ord(Phrasis[x])-97] += 1
            
        elif ord(Phrasis[x]) <= 90 and ord(Phrasis[x]) >=65:
            Letras[ord(Phrasis[x])-65] += 1
        
    Maior = Letras[0]
    for j in range(26):
        if  Letras[j] > Maior:
            Maior = Letras[j]
    
    if Maior != 0:
        for m in range(26):
            if Letras[m] == Maior:
                print(chr(m+97),end="")
    
    print()