import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

coord_x = (WIDTH//2)-50
coord_y = HEIGHT-120

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Figuras en movimiento")

running = True
#Bucle principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    #Lógica del juego
    coord_x += 1

    if coord_x > WIDTH:
        coord_x = -100

    #Zona de dibujo
    screen.fill(WHITE)

    pygame.draw.rect(screen,GREEN,(coord_x,coord_y,100,100))

    pygame.display.update()

    #Ralentizamos a 3 milisegundos cada vuelta del bucle
    pygame.time.delay(3)
    
pygame.quit()