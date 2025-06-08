import pygame, random

# Inicializar Pygame
pygame.init()

# Pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Colisiones visuales con rectángulos")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Clase Jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("arcade/arcade_pruebas/gato.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image.set_colorkey(BLANCO)
        # Ajustar el color clave para que el fondo sea transparente
        self.rect = self.image.get_rect()
        self.rect.center = ((ANCHO // 2), (ALTO - 60))
        self.velocidad = 5

    def update(self, teclas):
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.rect.x += self.velocidad
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.rect.y -= self.velocidad
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.rect.y += self.velocidad

# Clase Enemigo
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("arcade/arcade_pruebas/ratón.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()

# Grupos
todos_los_sprites = pygame.sprite.Group()
grupo_enemigos = pygame.sprite.Group()

# Instanciar sprites y añadirlos a los grupos
jugador = Jugador(todos_los_sprites)
enemigo = Enemigo(todos_los_sprites, grupo_enemigos)

for i in range(10):
    enemigo = Enemigo(todos_los_sprites, grupo_enemigos)
    enemigo.rect.x = random.randint(0, ANCHO - enemigo.rect.width)
    enemigo.rect.y = random.randint(0, ALTO - enemigo.rect.height)

# Bucle del juego
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    for enemigo in grupo_enemigos:
        enemigo.rect.y += 1
        if enemigo.rect.y > ALTO:
            enemigo.rect.y = 0

    teclas = pygame.key.get_pressed()
    jugador.update(teclas)

    colision = pygame.sprite.spritecollide(jugador, grupo_enemigos, True)

    # Cambiar fondo según colisión
    pantalla.fill(BLANCO)

    # Dibujar sprites
    todos_los_sprites.draw(pantalla)

    # Dibujar rectángulos de colisión en rojo
    #pygame.draw.rect(pantalla, ROJO, jugador.rect, 2)
    #pygame.draw.rect(pantalla, ROJO, enemigo.rect, 2)

    pygame.display.flip()

pygame.quit()
