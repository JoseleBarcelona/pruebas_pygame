import pygame
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
size_screen = (800,600)
x_rect = 50
y_rect = 50
x_speed = 3
y_speed = 3

screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption('figura rebotadora')
clock = pygame.time.Clock()

running = False
while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    x_rect += x_speed
    y_rect += y_speed

    if x_rect+50 > size_screen[0] or x_rect < 0:
        x_speed *= -1
    if y_rect+50 > size_screen[1] or y_rect < 0:
        y_speed *= -1

    screen.fill(BLACK)
    pygame.draw.rect(screen,WHITE,(x_rect,y_rect,50,50))
    pygame.draw.circle(screen,GREEN,(x_rect+25,y_rect+25),20)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()