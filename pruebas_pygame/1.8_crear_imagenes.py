import pygame, random

# Inicialización
pygame.init()

#Inicializamos el módulo de sonido
pygame.mixer.init()

# Constantes
BLACK = (0,0,0)
RED = (255,0,0)
screen = pygame.display.set_mode((920,800))
pygame.display.set_caption('Colisión parcial con meteoritos')
clock = pygame.time.Clock()

#Creamos un objeto que recibe un archivo .mp3
sonido_pong = pygame.mixer.Sound("/home/josele/Escritorio/pruebas_pygame/archivos_secuenciales/the-sound-of-hitting-the-ball.mp3")
# Imágenes
fondo = pygame.image.load("pruebas_pygame/universo.png").convert_alpha()
nave = pygame.image.load("pruebas_pygame/nave.jpg").convert()
nave.set_colorkey(BLACK)
nave_escalada = pygame.transform.scale(nave,(150,150))

meteorito = pygame.image.load("pruebas_pygame/meteorito.png").convert_alpha()
meteorito.set_colorkey(BLACK)
meteorito_escalado = pygame.transform.scale(meteorito,(75,75))

# Lista de meteoritos
lista_coordenadas = []
for i in range(8):
    coord_x = random.randint(0, 920 - 75)
    coord_y = random.randint(-800, 0)
    lista_coordenadas.append([coord_x, coord_y])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fondo, (0, 0))

    # Dibujar la nave
    nave_pantalla = screen.blit(nave_escalada, (350, 650))

    # Rect para la mitad inferior de la nave
    mitad_superior_nave = pygame.Rect(
        nave_pantalla.left,
        nave_pantalla.top + nave_pantalla.height-100,
        nave_pantalla.width,
        nave_pantalla.height // 2
    )

    # (Opcional) Mostrar la zona de colisión
    pygame.draw.rect(screen, RED, mitad_superior_nave, 2)  # borde rojo

    # Dibujar meteoritos y detectar colisiones
    for lista in lista_coordenadas[:]:  # recorrer copia
        meteorito_rect = screen.blit(meteorito_escalado, lista)
        lista[1] += 5

        if lista[1] > 800:
            lista[1] = random.randint(-100, -50)
            lista[0] = random.randint(0, 920 - 75)

        if mitad_superior_nave.colliderect(meteorito_rect):
            sonido_pong.play()
            lista_coordenadas.remove(lista)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
