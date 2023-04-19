a = [2,3,4,7]
# b=a Quando você iguala uma lista você esta fazendo uma ligação, não uma copia.
b = a[:]
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")