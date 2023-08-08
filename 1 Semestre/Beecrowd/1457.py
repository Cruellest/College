Instancias  = int(input())

for i in range(Instancias):
    entrada = input()
    Exclamacoes = "".join(entrada.split("!"))
    K = len(entrada) - len(Exclamacoes)
    N = int(Exclamacoes)
    SN = N
    cont = 1
    
    while N*(SN - (cont*K)) > 1:
         N = N*(SN-(cont*K))
         cont += 1

    print(N)