
import pygame

# Definimos algunos colores como constantes globales
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)

def main():
    """ Función principal del juego. """
    pygame.init()
    
    # Establecemos el largo y alto de la pantalla [largo,alto]
    dimensiones = [700, 500]
    pantalla = pygame.display.set_mode(dimensiones)

    pygame.display.set_caption("Mi Juego")

    #El bucle se ejecuta hasta que el usuario pincha sobre el botón de cierre.
    hecho = False

    # Se usa para establecer cuan rápido se actualiza la pantalla
    reloj = pygame.time.Clock()

    # -------- Bucle principal del Programa -----------
    while not hecho:
        # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR DEBAJO DE ESTE COMENTARIO
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                hecho = True
                
        # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR ENCIMA DE ESTE COMENTARIO
    
    
        # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO

        # TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO


        # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO

        # Primero, fijamos en blanco el fondo de pantalla. No escribas nada encima de este comando, de otra forma se borrará
        pantalla.fill(BLANCO)

        # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO

        # Avanzamos y actualizamos la pantalla que ya hemos dibujado
        pygame.display.flip()

        # Limitamos a 60 fps (frames por segundo)
        reloj.tick(60)

    # Cerrar la ventana y salir.
    # Si olvidas esto último, el programa se 'colgará' en la salida si lo llamamos desde el IDLE
    pygame.quit()

if __name__ == "__main__":
    main()
else:
    print("Este script no debería ser importado, ejecuta el archivo directamente.")
    exit(1)
# Fin del código
# Puedes añadir más funciones o clases aquí si lo necesitas.


