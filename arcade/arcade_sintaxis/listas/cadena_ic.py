from icecream import ic

cadena = 'Esto es un ejemplo de cadena de texto'
ic('La cadena es: ', cadena)
ic('cadena[0]= ', cadena[0])
ic('cadena[1]= ', cadena[1])
ic('cadena[-1]=', cadena[-1])
ic('cadena[:7]', cadena[:7])
ic('cadena[19:]', cadena[19:])
ic('cadena[8:19]', cadena[8:19])

a = ' Hola'
b = ' tú que'
c = ' ase!,'
ic(a+b+c)
ic((a+b+c)*3)
c = ' ase!\n'
ic((a+b+c)*3)

ic(f'La longitud de la cadena es de: {len(cadena)} caracteres incluidos los espacios')

for caracter in "Esto es una prueba":
    ic(caracter)
ic('\nFin de las pruebas con strings')

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