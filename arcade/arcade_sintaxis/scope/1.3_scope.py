x = 44
def funcion():
    print("Dentro de la función, x =", x)

funcion()

'''
Dentro de la función, x = 44
'''
# En este caso, la variable x se define en el ámbito global y se puede acceder a ella dentro de la función.
# Si se intenta modificar x dentro de la función, se debe declarar como global para evitar crear una nueva variable local.