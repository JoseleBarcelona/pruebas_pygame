import pygame, sys
from icecream import ic

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
pygame.display.set_caption('figuras')

#Aquí va la lógica (Un juego es un programa dentro de un bucle infinito)
while True:
    for event in pygame.event.get():
        ic(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(WHITE)

    ###----Zona de dibujo----###
    pygame.draw.line(screen,GREEN,(20,100),(200,100),5)
    pygame.draw.rect(screen,BLACK,(75,140,50,50))
    pygame.draw.circle(screen,BLUE,(100,250),30)
    pygame.draw.circle(screen,RED,(100,350),30,5)


    ###----Zona de dibujo----###

    #Actualiza la pantalla en cada vuelta del bucle
    pygame.display.flip()
