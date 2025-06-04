import pygame, sys, random

class Lluvia:
    def __init__(self):
        pygame.init()
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)
        self.size = (800,600)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('lluvia hecha con POO')
        self.bolas_aleatorias()

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            self.draw()
            pygame.display.flip()
            clock.tick(60)

    def bolas_aleatorias(self):
        self.lista_bolas = []
        for i in range(60):
                self.coord_x = random.randint(0, 800)
                self.coord_y = random.randint(0,600)
                self.lista_bolas.append([self.coord_x,self.coord_y])

    def handle_events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.screen.fill(self.WHITE)
        for lista in self.lista_bolas:
            pygame.draw.circle(self.screen,self.GREEN,lista,5)
            lista[1] += 3
            if lista[1] > 600:
                lista[1] = 0

if __name__ == "__main__":
    lluvia = Lluvia()
    lluvia.run()