x = 44
def funcion():
    global x
    x = 55
    print("Dentro de la función, x =", x)

funcion()
print("Fuera de la función, x =", x)

'''
Dentro de la función, x = 55
Fuera de la función, x = 55
'''
# En este ejemplo, la variable x se declara como global dentro de la función funcion().# Esto permite que la función modifique el valor de x en el ámbito global.
# Cuando se llama a funcion(), se imprime el valor de x dentro de la función y luego se imprime nuevamente fuera de la función.# El resultado muestra que el valor de x ha cambiado tanto dentro como fuera de la función.
# Esto demuestra cómo las variables globales pueden ser modificadas desde dentro de una función.
# Sin embargo, es importante tener cuidado al usar variables globales, ya que pueden hacer que el código sea más difícil de entender y mantener.
# Es recomendable limitar el uso de variables globales y, en su lugar, pasar argumentos a las funciones o devolver valores.

