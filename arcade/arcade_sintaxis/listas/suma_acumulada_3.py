lista = []
suma_lista = 0
numero = int(input('Escribe un número: '))
lista.append(numero)
for i in range(3):
    numero = int(input('Escribe otro número: '))
    lista.append(numero)

for i in lista:
    suma_lista += i

print(f'\nLa suma de la lista dada es de: {suma_lista}')

'''
Escribe un número: 10
Escribe otro número: 50
Escribe otro número: 40
Escribe otro número: 25

La suma de la lista dada es de: 125
'''