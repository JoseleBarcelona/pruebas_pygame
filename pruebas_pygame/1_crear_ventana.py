import pygame

pygame.init()

ventana = pygame.display.set_mode((800,600))

ventana.fill((0,255,0))
pygame.display.update()
pygame.time.delay(1500)
pygame.quit()