import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Matrix Binary Rain")

# Colores
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Fuente
font_size = 20
font = pygame.font.Font(None, font_size)

# Clase para una columna de lluvia binaria
class RainColumn:
    def __init__(self, x):
        self.x = x
        self.y = random.randint(-SCREEN_HEIGHT, 0)  # Empieza fuera de la pantalla
        self.speed = random.randint(5, 15)  # Velocidad de caída
        self.length = random.randint(10, 30)  # Longitud de la columna
        self.characters = [random.choice(['0', '1']) for _ in range(self.length)] # Caracteres binarios

    def fall(self):
        self.y += self.speed
        # Si la columna sale de la pantalla, la reiniciamos arriba con nuevos valores
        if self.y > SCREEN_HEIGHT:
            self.y = random.randint(-SCREEN_HEIGHT, 0)
            self.speed = random.randint(5, 15)
            self.length = random.randint(10, 30)
            self.characters = [random.choice(['0', '1']) for _ in range(self.length)]

    def draw(self, surface):
        for i, char in enumerate(self.characters):
            text_surface = font.render(char, True, GREEN)
            surface.blit(text_surface, (self.x, self.y + i * font_size))

# Crear las columnas de lluvia
columns = []
for i in range(0, SCREEN_WIDTH, font_size): # Espaciamos las columnas según el tamaño de la fuente
    columns.append(RainColumn(i))

# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rellenar el fondo de negro
    screen.fill(BLACK)

    # Actualizar y dibujar cada columna
    for column in columns:
        column.fall()
        column.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(30) # 30 frames por segundo

pygame.quit()