import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800,600
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("figuras geométricas")

running = True

#Bucle principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    #Zona de dibujos
    screen.fill(WHITE)
    
    pygame.draw.rect(screen,GREEN,(10,10,100,100),0,20)
    pygame.draw.rect(screen,RED,(690,10,100,100),8,20)
    pygame.draw.rect(screen,BLACK,(10,490,100,100))
    pygame.draw.rect(screen,BLUE,(690,490,100,100),0,20)
    pygame.draw.circle(screen,YELLOW,(60,60,),50)
    pygame.draw.circle(screen,BLUE,(60,60,),40)
    pygame.draw.rect(screen,RED,(35,35,50,50))
    pygame.draw.line(screen,BLACK,(110,110),(690,110),3)
    pygame.draw.line(screen,BLACK,(110,110),(110,490),3)
    pygame.draw.line(screen,BLACK,(110,490),(690,490),3)
    pygame.draw.line(screen,BLACK,(690,490),(690,110),3)
    pygame.draw.polygon(screen,BLUE,((300,300),(350,300),(350,250),(400,250),(400,300),(450,300),(450,350),(300,350)))

    #Actualización de la pantalla en cada vuelta del bucle
    pygame.display.update()

pygame.quit()