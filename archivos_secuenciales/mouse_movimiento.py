import pygame, sys
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
size_screen = (800,600)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption('Movimiento de figuras con el ratón')

#Definimos la visibilidad del mouse para no ver el cursor dentro de la pantalla
pygame.mouse.set_visible(0)

while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    #Con este método obtenemos las coordenadas a tiempo real de mi mouse
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    
    screen.fill(WHITE)

    pygame.draw.ellipse(screen,RED,(x,y,150,100))

    pygame.display.flip()
    clock.tick(60)