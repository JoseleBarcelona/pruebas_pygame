import pygame
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
ROJO = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CIAN = (52,235,229)

size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Figuras geométricas')
clock = pygame.time.Clock()
running = False

while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = True

    screen.fill(WHITE)

    for i in range(0, 101, 10):
        pygame.draw.line(screen,CIAN,(i,0),(i,100),3)
        pygame.draw.line(screen,BLUE,(0,100+i),(100,100+i),3)
        pygame.draw.line(screen,ROJO,(0, 0 + i),(100, 100 + i),3)
        
    pygame.draw.rect(screen,BLACK,(120,20,250,100),3)
    pygame.draw.ellipse(screen,BLACK,(120,20,250,100),3)
    pygame.draw.polygon(screen,GREEN,((100,200),(200,300),(0,300)),3)
        

    pygame.display.flip()
    clock.tick(60)

pygame.quit()