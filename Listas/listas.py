num =[2,5,9,1]
num[2] = 3
num.append(7)
num.insert(2, 0)
#append é para adicionar
num.sort()
num.pop()
num.remove(2)
if 9 in num:
    num.remove(9)
else:
    print("Não achei o numero ")
print(num)
print(len(num))
