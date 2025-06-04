import pygame, sys

class Animaciones:
    def __init__(self):
        pygame.init()
        self.size = (800,500)
        self.BLACK = (0,0,0,)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)
        self.coord_x = 0
        self.coord_y = 225
        self.speed_x = 5
        self.speed_y = 5
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Animaciones con programación orientada a objetos')

    def run(self):
        clock = pygame.time.Clock()

        while True:
            self.manejar_eventos()
            self.draw()
            pygame.display.flip()
            clock.tick(60)

    # Aquí va la lógica
    def manejar_eventos(self): 

        # Procesamos los eventos (teclado,mouse,cerrar ventana, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if (self.coord_x > 750 or self.coord_x <0):
            self.speed_x *= -1
        if (self.coord_y > 450 or self.coord_y <0):
            self.speed_y *= -1

        self.coord_x += self.speed_x
        self.coord_y += self.speed_y

    def draw(self):
        self.screen.fill(self.WHITE)
        pygame.draw.rect(self.screen,self.RED,(self.coord_x,self.coord_y,50,50))


if __name__ == "__main__":
    animaciones = Animaciones()
    animaciones.run()
