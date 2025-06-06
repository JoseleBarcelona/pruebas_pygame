# Pass-by-copy
# Las funciones pasan sus valores, creando copias del original.
# El valor de y no cambia a pesar de que la función f() incrementa el valor que le pasan. 
# Cada una de las variables listada como parámetro en una función, es una variable totalmente nueva. 
# El valor de la variable es copiado desde donde se le ha llamado.


def funcion(x):
    x *= 2
    return x

y = 5
print(funcion(y))  # Imprime 10

# Aquí, la variable y es global y se puede acceder a ella dentro de la función.
# Sin embargo, la variable x es un parámetro local de la función y no afecta a la variable global y.
# La función toma el valor de y, lo multiplica por 2 y devuelve el resultado.
# Por lo tanto, la variable y permanece sin cambios fuera de la función.