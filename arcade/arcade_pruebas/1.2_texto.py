import pygame
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
size = (800,600)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Incrustar texto')
clock = pygame.time.Clock()
contador = 0

#En la terminal puedes buscar las fuentes instaladas en el sistema con: fc-list
font = pygame.font.SysFont('Nimbus Mono PS',30)
text = font.render('Hello World!',True,BLUE)


running = False
while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = True
            if event.key == pygame.K_UP:
                contador += 1
            if event.key == pygame.K_DOWN:
                contador -= 1

    screen.fill(WHITE)
    screen.blit(text,(10,10))
    number = font.render(f'Contador {contador}',True,BLUE)
    screen.blit(number,(500,10))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()