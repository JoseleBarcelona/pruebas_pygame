import pygame, sys

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

size = (800,500)

coord_x = 10
coord_y = 10
x_speed = 3
y_speed = 3

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Movimiento de figuras con taclado')

clock = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Eventos de teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        coord_x -= x_speed
    if keys[pygame.K_RIGHT]:
        coord_x += x_speed
    if keys[pygame.K_UP]:
        coord_y -= y_speed
    if keys[pygame.K_DOWN]:
        coord_y += y_speed

    screen.fill(WHITE)
    
    pygame.draw.rect(screen,BLUE,(coord_x,coord_y,100,100))

    pygame.display.flip()
    clock.tick(60)