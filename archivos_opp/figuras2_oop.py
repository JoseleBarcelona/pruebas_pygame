import pygame, sys

class Figuras2:
    def __init__(self):
        pygame.init()
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)
        self.size = (800,600)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Figuras 2 hechas con POO')

    def run(self):
        while True:
            self.handle_events()
            self.draw()
            pygame.display.flip()

    def handle_events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()

    def draw(self):
        self.screen.fill(self.WHITE)
        for x in range(100,800,100):
            pygame.draw.line(self.screen,self.GREEN,(x,50),(x,175),5)
            pygame.draw.circle(self.screen,self.RED,(x,250),30)
            pygame.draw.circle(self.screen,self.BLUE,(x,350),30,5)

if __name__ == '__main__':
    figuras2 = Figuras2()
    figuras2.run()