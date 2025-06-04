import pygame, sys

# Inicializamos la librería de pygame
pygame.init()

#Inicializamos el módulo de sonido
pygame.mixer.init()

# Inicializamos una fuente para el marcador
pygame.font.init()
font = pygame.font.SysFont('Arial', 40)

# Puntos de cada jugador
score_player1 = 0
score_player2 = 0


# Creamos unas constantes de colores
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE_SKY = (0,255,255)
WIDTH, HEIGHT = 1000, 600

# Creamos la ventana de juego
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de ping-pong")

# Creamos un objeto de la subclase Clock
clock = pygame.time.Clock()

#Creamos dos objetos que reciben un archivo .mp3
sonido_pong = pygame.mixer.Sound("/home/josele/Escritorio/pruebas_pygame/archivos_secuenciales/the-sound-of-hitting-the-ball.mp3")
sonido_marcador = pygame.mixer.Sound("/home/josele/Escritorio/pruebas_pygame/archivos_secuenciales/ringing-sound-on-sms-for-phone.mp3")


# Tamaño de los jugadores (es el mismo en ambos casos)
player_width, player_height = 10, 100

# Coordenadas y velocidad del jugador 1
player1_x_coord = 10
player1_y_coord = (HEIGHT // 2) - (player_height // 2)
player1_speed_y = 0

# Coordenadas y velocidad del jugador 2
player2_x_coord = WIDTH - player_width - 10
player2_y_coord = (HEIGHT // 2) - (player_height // 2)
player2_speed_y = 0

# Tamaño, coordenadas y velocidad de la pelota
ball_size = 7
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 6, 6

# Creamos el bucle infinito donde se ejecutará el juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Detectamos las teclas pulsadas para mover los jugadores arriba o abajo
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player1_speed_y = -5
    if keys[pygame.K_z]:
        player1_speed_y = 5
    if keys[pygame.K_UP]:
        player2_speed_y = -5
    if keys[pygame.K_DOWN]:
        player2_speed_y = 5

    # Actualizamos las coordenadas en el eje Y para que los jugadores paren al soltar las teclas
    player1_y_coord += player1_speed_y
    player1_speed_y = 0
    player2_y_coord += player2_speed_y
    player2_speed_y = 0

    # Evitamos que el jugador 1 se salga de la pantalla
    if player1_y_coord < 0:
        player1_y_coord = 0
    if player1_y_coord > HEIGHT - player_height:
        player1_y_coord = HEIGHT - player_height

    # Evitamos que el jugador 2 se salga de la pantalla
    if player2_y_coord < 0:
        player2_y_coord = 0
    if player2_y_coord > HEIGHT - player_height:
        player2_y_coord = HEIGHT - player_height

    # Movimiento de la pelota
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Rebote vertical de la pelota para que no se salga de la pantalla en el eje 'Y'
    if ball_y > (HEIGHT - ball_size) or ball_y < 0:
        ball_speed_y *= -1

    # Si la pelota se va por la derecha, punto para el jugador 1
    if ball_x > WIDTH:
        score_player1 += 1
        sonido_marcador.play()
        ball_x = 35
        ball_y = (HEIGHT//2) - (player_height//2)
    #Lo multiplicamos po 1 para que saque el jugador que gana
        ball_speed_x *= 1
        ball_speed_y *= 1
    # Si se va por la izquierda, punto para el jugador 2
    elif ball_x < 0:
        score_player2 += 1
        sonido_marcador.play()
        ball_x = (WIDTH - player_width - 25)
        ball_y = (HEIGHT//2 - player_height//2)
    #Lo multiplicamos po 1 para que saque el jugador que gana
        ball_speed_x *= 1
        ball_speed_y *= 1

    #Cuando uno de los jugadores llega a 5 puntos, el marcador se reinicia
    if score_player1 == 5 or score_player2 == 5:
        pygame.time.delay(1500)
        score_player1 = 0
        score_player2 = 0
        ball_x = WIDTH//2
        ball_y = HEIGHT//2


    # Rellenamos el fondo del color de la ventana del juego
    screen.fill(BLACK)

    # Dibujamos los jugadores y la pelota
    player1 = pygame.draw.rect(screen, BLUE_SKY, (player1_x_coord, player1_y_coord, player_width, player_height))
    player2 = pygame.draw.rect(screen, BLUE_SKY, (player2_x_coord, player2_y_coord, player_width, player_height))
    ball = pygame.draw.circle(screen,BLUE_SKY, (ball_x, ball_y), ball_size)
    linea = pygame.draw.line(screen,BLUE_SKY,(WIDTH//2,(0+15)),(WIDTH//2,HEIGHT-15),4)

    # Detectamos colisiones entre la pelota y los jugadores
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1
        sonido_pong.play()

    # Renderizamos el texto con los puntajes
    score_text = font.render(f"{score_player1}    {score_player2}", True, WHITE)
    # Lo dibujamos centrado arriba
    screen.blit(score_text, ((WIDTH // 2) - score_text.get_width() // 2, 20))


    # Actualizamos la pantalla
    pygame.display.flip()

    # Control de FPS
    clock.tick(60)
