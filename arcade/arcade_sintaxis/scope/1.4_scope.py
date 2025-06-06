x = 44
def funcion():
    x = 55
    print("Dentro de la función, x =", x)

funcion()
print("Fuera de la función, x =", x)

'''
Dentro de la función, x = 55
Fuera de la función, x = 44
'''

# En este caso, la variable x se define dentro de la función, lo que crea una variable local que oculta la variable global x.
# Cuando se imprime x dentro de la función, se muestra el valor local (55), mientras que fuera de la función se muestra el valor global (44).
# Esto demuestra cómo las variables locales pueden ocultar las variables globales con el mismo nombre.
# Es importante tener en cuenta que las variables locales solo son accesibles dentro de la función donde se definen.
# Si se intenta acceder a x fuera de la función, se obtendrá el valor de la variable global, ya que la variable local solo existe dentro del ámbito de la función.
# Esto es útil para evitar conflictos de nombres y mantener el código más organizado.
# Sin embargo, si se desea modificar la variable global x desde dentro de la función, se debe declarar como global.
# Esto permite que la función modifique el valor de la variable global en lugar de crear una nueva variable local.
# En general, es una buena práctica evitar el uso de variables globales siempre que sea posible, ya que pueden hacer que el código sea más difícil de entender y mantener.
# En su lugar, es recomendable pasar argumentos a las funciones o devolver valores.
# Esto ayuda a mantener el código más limpio y modular, lo que facilita su comprensión y mantenimiento a largo plazo.
# Además, el uso de variables globales puede llevar a errores difíciles de rastrear si se modifican accidentalmente en diferentes partes del código.
# Por lo tanto, es recomendable utilizar variables locales siempre que sea posible y limitar el uso de variables globales a situaciones específicas donde realmente se necesiten.
# En resumen, las variables locales y globales tienen diferentes ámbitos y propósitos en el código.

