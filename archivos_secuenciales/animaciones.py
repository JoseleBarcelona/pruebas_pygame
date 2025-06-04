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
pygame.display.set_caption('Animación')

#Creamos un objeto reloj para contorlar los Frames per second FPS
clock = pygame.time.Clock()

#Definimos las coordenadas de inicio
coord_x = 0
coord_y = 225

#Definimos los pixeles de movimiento que queremos aumentar en cada vuelta del bucle
speed_x = 5
speed_y = 5

#Aquí va la lógica (Un juego es un programa dentro de un bucle infinito)
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

    if (coord_x > 750 or coord_x <0):
        speed_x *= -1
    if (coord_y > 450 or coord_y <0):
        speed_y *= -1

    coord_x += speed_x
    coord_y += speed_y

    #Damos el color de fondo a la pantalla
    screen.fill(WHITE)

    ###----Zona de dibujo----###
    pygame.draw.rect(screen,RED,(coord_x,coord_y,50,50))


    ###----Zona de dibujo----###

    #Actualiza la pantalla en cada vuelta del bucle
    pygame.display.flip()

    #Pasamos valores al objeto reloj
    clock.tick(60)
