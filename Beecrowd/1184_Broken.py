ty = input()

if ty == "S":
    cont = 0
    l = 0
    for i in range(144):
        a = float(input())
        if i == cont:
            l = l+a
            cont = cont+13

elif ty == "M":
    cont = 0
    l = 0
    for i in range(144):
        a = float(input())
        if i == cont:
            l = l + a
            cont = cont + 13
    l = l/12

print(l)