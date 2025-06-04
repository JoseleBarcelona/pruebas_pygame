import pygame, sys

class Mouse:
    def __init__(self):
        pygame.init()
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)
        self.size = (800,600)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Movimiento de figuras con el ratón con POO')
        pygame.mouse.set_visible(0)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            self.posicion_mouse()
            self.draw()
            pygame.display.flip()
            clock.tick(60)

    def handle_events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def posicion_mouse(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.x = self.mouse_pos[0]
        self.y = self.mouse_pos[1]

    def draw(self):
        self.screen.fill(self.WHITE)
        pygame.draw.ellipse(self.screen,self.RED,(self.x,self.y,150,100))

if __name__ == "__main__":
    mouse = Mouse()
    mouse.run()