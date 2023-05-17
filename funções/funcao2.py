def contador(*num):
    print(num)


contador(2, 1, 3)
contador(3, 4, 5)
contador(5, 6, 7)


def soma(*valor):
    s= 0
    for num in valor:
        s+=num
    print(f"Somando os valores {valor} temos {s}")


soma(1,5,6)
soma(1,3,4,5,6,7)