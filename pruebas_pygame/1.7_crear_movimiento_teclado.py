import pygame
pygame.init()

screen_size = (800,600)

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

x_asteroide = 10
y_asteroride = 50
x_nave = (screen_size[0]//2)-25
y_nave = (screen_size[1]-20-50)

x_asteroride_speed = 5
x_nave_speed = 5
y_nave_speed = 5

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Mover figuras con el teclado")
clock = pygame.time.Clock()

direccion = "arriba"
contador = 0

#Funciones
def nave_arriba(superficie,x,y):
    pygame.draw.rect(superficie,GREEN,(x,y,50,50))

    #Dibujamos 2 rectángulos blancos superponiéndolos al cuadrado mayor
    pygame.draw.rect(superficie,WHITE,(x,y,15,25))
    pygame.draw.rect(superficie,WHITE,(x+35,y,15,25))

def nave_abajo(superficie,x,y):
    pygame.draw.rect(superficie,GREEN,(x,y,50,50))
    pygame.draw.rect(superficie,WHITE,(x,y+25,15,25))
    pygame.draw.rect(superficie,WHITE,(x+35,y+25,15,25))

def nave_derecha(superficie,x,y):
    pygame.draw.rect(superficie,GREEN,(x,y,50,50))
    pygame.draw.rect(superficie,WHITE,(x+25,y,25,15))
    pygame.draw.rect(superficie,WHITE,(x+25,y+35,25,15))

def nave_izquierda(superficie,x,y):
    pygame.draw.rect(superficie,GREEN,(x,y,50,50))
    pygame.draw.rect(superficie,WHITE,(x,y,25,15))
    pygame.draw.rect(superficie,WHITE,(x,y+35,25,15))

def asteroide_1(superficie,x,y):
    pygame.draw.rect(superficie,RED,(x,y,50,50))
    pygame.draw.rect(superficie,WHITE,(x,y,20,20))

def asteroide_2(superficie,x,y):
    pygame.draw.rect(superficie,RED,(x,y,50,50))
    pygame.draw.rect(superficie,WHITE,(x+30,y,20,20))

def asteroide_3(superficie,x,y):
    pygame.draw.rect(superficie,RED,(x,y,50,50))
    pygame.draw.rect(superficie,WHITE,(x+30,y+30,20,20))

def asteroide_4(superficie,x,y):
    pygame.draw.rect(superficie,RED,(x,y,50,50))
    pygame.draw.rect(superficie,WHITE,(x,y+30,20,20))


#Bucle principal
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    #Damos velocidad constante al asteroide
    x_asteroide += 3
    if x_asteroide > screen_size[0]:
        x_asteroide = -50

    #Movemos la nave con las teclas presionadas
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        direccion = "izquierda"
        x_nave -= x_nave_speed
    if key[pygame.K_RIGHT]:
        direccion = "derecha"
        x_nave += x_nave_speed
    if key[pygame.K_UP]:
        direccion = "arriba"
        y_nave -= y_nave_speed
    if key[pygame.K_DOWN]:
        direccion = "abajo"
        y_nave += y_nave_speed

    #Delimitamos que la nave no se salga de la pantalla
    if x_nave > screen_size[0]-50:
        x_nave = screen_size[0]-50
    elif x_nave < 0:
        x_nave = 0
    if y_nave > screen_size[1]-50:
        y_nave = screen_size[1]-50
    elif y_nave < 0:
        y_nave = 0

    screen.fill(WHITE)
    
    #Llamadas a las funciones (ZONA DE DIBUJO)
    if direccion == "arriba":
        nave_arriba(screen, x_nave, y_nave)
    elif direccion == "abajo":
        nave_abajo(screen,x_nave,y_nave)
    elif direccion == "derecha":
        nave_derecha(screen,x_nave,y_nave)
    elif direccion == "izquierda":
        nave_izquierda(screen,x_nave,y_nave)

    contador += 1

    if contador > 41:
        contador = 1

    if contador < 11:
        asteroide_1(screen,x_asteroide,y_asteroride)
    elif contador < 21:
        asteroide_2(screen,x_asteroide,y_asteroride)
    elif contador < 31:
        asteroide_3(screen,x_asteroide,y_asteroride)
    elif contador < 41:
        asteroide_4(screen,x_asteroide,y_asteroride)

    pygame.display.update()
    clock.tick(60)
pygame.quit()