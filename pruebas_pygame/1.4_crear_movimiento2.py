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

rect1_x = (WIDTH//2)-50
rect1_y = HEIGHT-120
rect2_x = 200
rect2_y = 200

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
    rect1_x -= 1
    if rect1_x < -50:
        rect1_x = WIDTH

    rect2_x += 1
    rect2_y += 1
    if rect2_x > WIDTH:
        rect2_x = -50
    if rect2_y > HEIGHT:
        rect2_y = -50

    #Zona de dibujo
    screen.fill(WHITE)

    pygame.draw.rect(screen,GREEN,(rect1_x,rect1_y,50,50))
    pygame.draw.rect(screen,BLUE,(rect2_x,rect2_y,50,50))

    pygame.display.update()

    #Ralentizamos a 3 milisegundos cada vuelta del bucle
    pygame.time.delay(3)
    
pygame.quit()