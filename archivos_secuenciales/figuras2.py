import pygame, sys

#Inicializamos la librería pygame
pygame.init()

#Definimos constantes de colores en RGB
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Asignamos el tamaño de la pantalla con una tupla
size = (800,500)

#Creamos una ventana
screen = pygame.display.set_mode(size)
pygame.display.set_caption('figuras aleatorias')

#Aquí va la lógica (Un juego es un programa dentro de un bucle infinito)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(WHITE)

    ###----Zona de dibujo----###
    for x in range(100,800,100):
        pygame.draw.circle(screen,BLUE,(x,250),30)
        pygame.draw.circle(screen,RED,(x,350),30,5)
        pygame.draw.line(screen,GREEN,(x,50),(x,175),5)


    ###----Zona de dibujo----###

    #Actualiza la pantalla en cada vuelta del bucle
    pygame.display.flip()
