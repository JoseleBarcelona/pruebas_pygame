import pygame
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CIAN = (52,235,229)

size = (850,780)
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

    for i in range(0, 121, 10):
        pygame.draw.rect(screen,BLACK,(10+i,10+i,250,100),2)
        pygame.draw.ellipse(screen,BLACK,(10,280+i,250,100),2)
        pygame.draw.polygon(screen,BLACK,((600,10+i),(700,100+i),(500,100+i)),2)
        pygame.draw.ellipse(screen,BLACK,(320+i,290+i,250+i,100+i*2),2)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()