Lista = []

for c in range(0,5):
    n = int(input("Digite um valor: "))
    if(c == 0 or n > Lista[-1]):
        Lista.append(n)
    else:
        pos = 0
        while pos < len(Lista):
            if n <= Lista[pos]:
                Lista.insert(pos,n)
                break
            pos +=1
            
print(Lista)