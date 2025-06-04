import pygame

#Inicializar
pygame.init()

#Medidas
ANCHO = 800
ALTO = 600

#Colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)
VERDE = (0,255,0)
BLUE_SKY = (0,255,255)
PURPLE = (255,0,255)
YELLOW = (255,255,0)

#Ventana
ventana = pygame.display.set_mode((ANCHO,ALTO))

jugando = True

#Bucle principal
while jugando:
    #Eventos
    for evento in pygame.event.get():
        #print(evento)
        if evento.type == pygame.QUIT:
            jugando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                jugando = False

    #Dibujos
    ventana.fill(BLUE_SKY)

    #Actualizar
    pygame.display.update()

#Salir
pygame.quit()