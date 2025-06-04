meses = "EneFebMarAbrMayJunJulAgoSepOctNovDic"

while True:
    entrada = input("Introduce el número de mes (1-12) o escribe 'salir' para terminar: ")

    if entrada.lower() == "salir":
        print("¡Gracias por jugar! Hasta la próxima.")
        break
    try:
        n = int(entrada)
        
        if n == 1:
            print(meses[0:3])
        elif n == 2:
            print(meses[3:6])
        elif n == 3:
            print(meses[6:9])
        elif n == 4:
            print(meses[9:12])
        elif n == 5:
            print(meses[12:15])
        elif n == 6:
            print(meses[15:18])
        elif n == 7:
            print(meses[18:21])
        elif n == 8:
            print(meses[21:24])
        elif n == 9:
            print(meses[24:27])
        elif n == 10:
            print(meses[27:30])
        elif n == 11:
            print(meses[30:33])
        elif n == 12:
            print(meses[33:36])
        else:
            print("Número de mes no válido. Debe estar entre 1 y 12.")
    except ValueError:
        print('Debe introducir un número entero')