def funcion():
    x = 10
    print("Dentro de la función, x =", x)

funcion()
#print(x)  # Esto causará un error porque x no está definido en el ámbito global

'''
Dentro de la función, x = 10
Traceback (most recent call last):
  File "/home/josele/Escritorio/pruebas_pygame/arcade/arcade_sintaxis/scope/1.2_scope.py", line 6, in <module>
    print(x)  # Esto causará un error porque x no está definido en el ámbito global
          ^
NameError: name 'x' is not defined

'''