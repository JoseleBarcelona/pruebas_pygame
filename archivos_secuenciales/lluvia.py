import pygame, sys, random
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
size = (800,600)


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lluvia de bolas")
clock = pygame.time.Clock()

lista_bolas = []
for i in range(60):
        coord_x = random.randint(0, 800)
        coord_y = random.randint(0,600)
        lista_bolas.append([coord_x,coord_y])

while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(WHITE)

    for lista in lista_bolas:
        pygame.draw.circle(screen,GREEN,lista,5)
        lista[1] += 3
        if lista[1] > 600:
            lista[1] = 0
        
    pygame.display.flip()
    clock.tick(60)