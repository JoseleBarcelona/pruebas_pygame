meses = "EneFebMarAbrMayJunJulAgoSepOctNovDic"

while True:
    entrada = input("Introduce el número de mes (1-12) o escribe 'salir' para terminar: ")

    if entrada.lower() == "salir":
        print("¡Gracias por jugar! Hasta la próxima.")
        break
    try:
        n = int(entrada)
        
        if 1 <= n <= 12:
            inicio = (n - 1) * 3
            fin = inicio + 3
            print(meses[inicio:fin])
        else:
            print("Número de mes no válido. Debe estar entre 1 y 12.")
    except ValueError:
        print('Debe introducir un número entero.')

'''
¿Qué cambios hice y por qué?

    Eliminación de la cadena if/elif larga: 
    En lugar de tener una condición if para cada mes, ahora calculamos el inicio y el fin del segmento de la cadena meses de forma dinámica.
        Cada mes tiene 3 caracteres. Si el usuario ingresa 1 (enero), queremos 0:3. Si ingresa 2 (febrero), queremos 3:6, y así sucesivamente.
        La fórmula (n - 1) * 3 nos da el índice de inicio correcto. Por ejemplo, para el mes 1, (1-1)*3 = 0. Para el mes 2, (2-1)*3 = 3.
        El índice de fin es simplemente inicio + 3.
    Validación de entrada: Simplifiqué la validación del rango de meses a 1 <= n <= 12, que es más conciso y fácil de leer.

Esta versión es mucho más escalable. Si quisieras añadir más "ítems" a tu cadena en el futuro, no tendrías que añadir un elif más por cada uno, solo modificar la lógica del cálculo.
'''