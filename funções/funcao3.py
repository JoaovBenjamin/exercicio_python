def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos+=1

valor = [1,2,3,4,5]
dobra(valor)
print(valor)