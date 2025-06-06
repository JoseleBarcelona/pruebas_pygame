# Pass-by-copy
# Las funciones pasan sus valores, creando copias del original.
# El valor de x no cambia a pesar de que la función f() incrementa el valor que le pasan. 
# Cada una de las variables listada como parámetro en una función, es una variable totalmente nueva. 
# El valor de la variable es copiado desde donde se le ha llamado.

def funcion(x):
    x *= 2
    return x    

x = 5
print(funcion(x))  # Imprime 10

# Aquí, la variable x es global y se puede acceder a ella dentro de la función.
# Sin embargo, la variable x es un parámetro local de la función y no afecta a la variable global x.
# La función toma el valor de x, lo multiplica por 2 y devuelve el resultado.
# Por lo tanto, la variable x permanece sin cambios fuera de la función.