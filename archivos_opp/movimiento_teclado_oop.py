import pygame, sys

class Teclado:
    def __init__(self):
        pygame.init()
        #Colores
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)
        #Tamaño pantalla
        self.width = 800
        self.height = 600
        #Tamaño figura
        self.shape_width = 100
        self.shape_height = 100
        #Coordenadas y velocidad
        self.coord_x = (self.width//2)-(self.shape_width//2)
        self.coord_y = (self.height//2)-(self.shape_height//2)
        self.x_speed = 10
        self.y_speed = 10
        #Creación de pantalla
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Movimiento de la figura con teclado')
        
    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            self.draw()
            self.key_pressed()
            pygame.display.flip()
            clock.tick(60)
    
    def handle_events(self):
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def key_pressed(self):
        #Detección de las teclas pulsadas
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_LEFT]:
            self.coord_x -= self.x_speed
        if self.keys[pygame.K_RIGHT]:
            self.coord_x += self.x_speed
        if self.keys[pygame.K_UP]:
            self.coord_y -= self.y_speed
        if self.keys[pygame.K_DOWN]:
            self.coord_y += self.y_speed

        #Limitar que la figura no se salga de la pantalla
        if self.coord_x < 0:
            self.coord_x = 0
        if self.coord_x > (self.width - self.shape_width):
            self.coord_x = (self.width - self.shape_height)
        if self.coord_y < 0:
            self.coord_y = 0
        if self.coord_y > (self.height - self.shape_height):
            self.coord_y = (self.height - self.shape_height)

    def draw(self):
        self.screen.fill(self.WHITE)
        pygame.draw.rect(self.screen,self.BLUE,(self.coord_x,self.coord_y,self.shape_width,self.shape_height))

if __name__ == "__main__":
    teclado = Teclado()
    teclado.run()