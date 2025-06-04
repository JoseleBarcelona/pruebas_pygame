import pygame

#Inicializar librería
pygame.init()

#Inicializar módulo fuentes
pygame.font.init()

#Variables globales
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

BLACK = (0,0,0,)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE_SKY = (0,255,255)
PURPLE = (255,0,255)
YELLOW = (255,255,0)

coord_x = (SCREEN_WIDTH//2-25)
coord_y = SCREEN_HEIGHT-100
speed_x = 1
vueltas = 0

#Creación de ventana
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Añadir texto")

#Creación de superficie donde pegar el texto
font = pygame.font.SysFont("Arial",25)

#Renderizado del texto sobre la superficie creada
text = font.render("CUADRADOS",True,WHITE)

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
    
    if coord_x > SCREEN_WIDTH:
        coord_x = -50
        vueltas += 1

    coord_x += speed_x

#Dibujos sobre la ventana
    screen.fill(BLACK)
    pygame.draw.rect(screen,BLUE_SKY,(coord_x,coord_y,50,50))

    #Renderizado del marcador sobre la superficie creada
    marcador1 = font.render(f"Vueltas:  {vueltas}",True,PURPLE)

    #Pegar el texto y el marcador sobre la ventana del juego
    screen.blit(text, ((SCREEN_WIDTH // 2) - (text.get_width()//2), 20))
    screen.blit(marcador1,(20,20))

#Actualización de ventana y temporizador del bucle
    pygame.display.update()
    pygame.time.delay(3)

#Salir del juego
pygame.quit()