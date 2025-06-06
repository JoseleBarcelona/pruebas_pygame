x = 44
def funcion():
    #x += 1
    print("Dentro de la función, x =", x)

funcion()
print("Fuera de la función, x =", x)

'''Dentro de la función, x = 45
Traceback (most recent call last):
  File "1.6_scope.py", line 6, in <module>
    funcion()
  File "1.6_scope.py", line 3, in funcion
    x += 1
UnboundLocalError: local variable 'x' referenced before assignment
'''
# En este caso, se produce un error porque la variable x se intenta modificar dentro de la función sin haber sido declarada como global.
# Python interpreta que x es una variable local debido al uso de la asignación x += 1, pero no se ha inicializado antes de su uso.
# Para solucionar este problema, se debe declarar x como global dentro de la función si se desea modificar la variable global.
# O se puede dar un valor inicial a x dentro de la función antes de modificarla.





