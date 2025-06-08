import pygame
pygame.init()

# Configuración de la ventana
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sprite Cuadrado")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
FPS = 60

# Clase para el sprite cuadrado
class Jugador(pygame.sprite.Sprite):
    def __init__(self, *groups, color=ROJO, tamaño=(50, 50)):
        super().__init__(*groups)
        self.image = pygame.Surface(tamaño)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO // 2)
        self.velocidad = 5

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidad
        # Limitar el movimiento dentro de la ventana
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
            
# Clase para el enemigo
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, *groups, color=AZUL, tamaño=(50, 50)):
        super().__init__(*groups)
        self.image = pygame.Surface(tamaño)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)

    def update(self):
        # Aquí podrías agregar lógica para el enemigo
        pass
# Inicializar el sprite
todos_los_sprites = pygame.sprite.Group()
grupo_enemigos = pygame.sprite.Group()
jugador = Jugador(todos_los_sprites, color=ROJO, tamaño=(50, 50))
enemigo = Enemigo(grupo_enemigos, color=AZUL, tamaño=(50, 50))


# Bucle principal del juego
reloj = pygame.time.Clock()
corriendo = True
while corriendo:
    reloj.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Actualizar sprites
    todos_los_sprites.update()

    #colisión entre jugador y enemigos
    colisiones = pygame.sprite.spritecollide(jugador, grupo_enemigos, False)
    
    # Dibujar todo
    if colisiones:
        ventana.fill(VERDE)  # Cambiar el color de fondo si hay colisión
    else:
        ventana.fill(NEGRO)
    todos_los_sprites.draw(ventana)
    grupo_enemigos.draw(ventana)
    pygame.display.flip()

pygame.quit()