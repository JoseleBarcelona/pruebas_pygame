import pygame, random
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 20)

#Variables globales
size = (800,600)
BLACK = (0,0,0,)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE_SKY = (0,255,255)
PURPLE = (255,0,255)
YELLOW = (255,255,0)

#Creación de ventana
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lluvia")
clock = pygame.time.Clock()



esferas = []
for i in range(100):
    coord_x = random.randint(0,800)
    coord_y = random.randint(0,600)
    coord = [coord_x,coord_y]
    esferas.append(coord)

running = True

#Bucle principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

#Dibujos sobre la ventana
    screen.fill(BLACK)

    for lista in esferas:
        pygame.draw.circle(screen,PURPLE,lista,5)
        lista[0] += 1
        lista[1] += 1
        if lista[0] > 800:
            lista[0] = 0
        if lista[1] > 600:
            lista[1] = 0

    ticks = font.render(f"Ticks por frame:   {pygame.time.get_ticks()}", True, BLUE_SKY)
    frames = font.render(f"Frames por segundo:  {pygame.time.Clock.get_fps(clock)}", True, BLUE_SKY)
    screen.blit(ticks,(10,10))
    screen.blit(frames,(450,10))

#Actualización de ventana
    pygame.display.update()
    clock.tick(60)

#Salir del juego
pygame.quit()