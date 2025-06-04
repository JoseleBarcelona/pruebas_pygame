import pygame,random
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
size = (800,600)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
y_speed = 3

bolas = []
for i in range(50):
    x = random.randrange(0,800)
    y = random.randrange(0,600)
    coord = [x,y]
    bolas.append(coord)
print(f'\nCreamos 1 lista con 50 listas de coordenadas aleatorias:\n\n {bolas}'.upper())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    for nieve in bolas:
        pygame.draw.circle(screen,WHITE,(nieve[0],nieve[1]),3)
        nieve[1] += y_speed
        if nieve[1] > 600 or nieve[1] == 0:
            nieve[1] = 0

    pygame.display.flip()
    clock.tick(60)

pygame.quit()