lista = []
numeros = int(input('Escribe un número: '))
lista.append(numeros)
for i in range(3):
    numeros = int(input('Escribe otro número: '))
    lista.append(numeros)
print(f'\nlista = {lista}')

'''
Escribe un número: 56
Escribe otro número: 87
Escribe otro número: 42
Escribe otro número: 98
[56, 87, 42, 98]
'''