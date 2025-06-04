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

#funciones
def snowman(screen,x,y):
    pygame.draw.circle(screen,WHITE,(50+x,25+y),20)
    pygame.draw.circle(screen,WHITE,(50+x,70+y),30)
    pygame.draw.circle(screen,WHITE,(50+x,125+y),40)
    pygame.draw.line(screen,WHITE,(5+x,40+y),(20+x,60+y),3)
    pygame.draw.line(screen,WHITE,(95+x,40+y),(79+x,60+y),3)

#Aquí va la lógica (Un juego es un programa dentro de un bucle infinito)
while True:
    for event in pygame.event.get():
        ic(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(BLACK)

    ###----Zona de dibujo----###
    snowman(screen,0,0)
    snowman(screen,200,0)
    snowman(screen,200,200)
    snowman(screen,600,200)


    ###----Zona de dibujo----###

    #Actualiza la pantalla en cada vuelta del bucle
    pygame.display.flip()
