
#ord(): Obtenemos el valor Unicode (o el valor ordinal del punto de código ASCII, si el carácter está dentro del rango ASCII) de un solo carácter.
#chr(): Hace exactamente lo contrario. Se utiliza para obtener el carácter Unicode (o el carácter ASCII, si el número está dentro del rango ASCII) 

texto_plano = "Esto es una prueba. ABC abc"

for c in texto_plano:
    print (c, end="")
print()
#Esto es una prueba. ABC abc

for c in texto_plano:
    print (ord(c), end=" ")
print()
#69 115 116 111 32 101 115 32 117 110 97 32 112 114 117 101 98 97 46 32 65 66 67 32 97 98 99

for c in texto_plano:
    x = ord(c)
    x += 1
    print(x, end=' ')
print()
#70 116 117 112 33 102 116 33 118 111 98 33 113 115 118 102 99 98 47 33 66 67 68 33 98 99 100 

for c in texto_plano:
    x = ord(c) #Lo convertimos al valor ordinal
    y = chr(x) #Lo volvemos a convertir al valor del caracter
    print(y, end='')
print()
#Esto es una prueba. ABC abc

for c in texto_plano:
    x = ord(c)
    x = x + 1
    y = chr(x)
    print(y, end='')
print()
#Ftup!ft!vob!qsvfcb/!BCD!bcd

encriptacion = 'Ftup!ft!vob!qsvfcb/!BCD!bcd'
for c in encriptacion:
    x = ord(c)
    x = x - 1
    y = chr(x)
    print(y, end='')
print()
#Esto es una prueba. ABC abc

# Crea un array asociativo vacío (Diccionario)
# (Observar las llaves.)
x = {}

# Añadirle algo
x["fred"] = 2 #clave:valor  key:value
x["scooby"] = 8
x["wilma"] = 1

# Obtener e imprimir un item
print(x["fred"]) #2
print(x) #{'fred': 2, 'scooby': 8, 'wilma': 1}
