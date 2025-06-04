
cadena = 'Esto es un ejemplo de cadena de texto'
print('La cadena es: ', cadena)
print('cadena[0]= ', cadena[0])
print('cadena[1]= ', cadena[1])
print('cadena[-1]=', cadena[-1])
print('cadena[:7]', cadena[:7])
print('cadena[19:]', cadena[19:])
print('cadena[8:19]', cadena[8:19])

a = ' Hola'
b = ' tú que'
c = ' ase!,'
print(a+b+c)
print((a+b+c)*3)
c = ' ase!\n'
print((a+b+c)*3)

print(f'La longitud de la cadena es de: {len(cadena)} caracteres incluidos los espacios')

for caracter in "Esto es una prueba":
    print(caracter, end='')
print('\nFin de las pruebas con strings')

'''
La cadena es:  Esto es un ejemplo de cadena de texto
cadena[0]=  E
cadena[1]=  s
cadena[-1]= o
cadena[:7] Esto es
cadena[19:] de cadena de texto
cadena[8:19] un ejemplo 
Hola tú que ase!,
Hola tú que ase!, Hola tú que ase!, Hola tú que ase!,
Hola tú que ase!
Hola tú que ase!
Hola tú que ase!

La longitud de la cadena es de: 37 caracteres incluidos los espacios
Esto es una prueba
Fin de las pruebas con strings
'''