import pygame, sys

# Creamos la clase principal del juego
class Figuras:
    # Inicializamos el constructor de la clase Game
    def __init__(self):

        # Inicializamos pygame
        pygame.init()

        # Definimos el tamaño de la ventane
        self.size = (800,600)

        # Definimos los colores
        self.BLACK = (0,0,0,)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)

        # Creamos la ventana (pantalla)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('figuras con programación orientada a objetos')

        # Controlamos si el juego sigue ejecutándose
        self.running = True

    # Creamos la función que llamará a los métodos que se deben ejecutar
    def run(self):

        # Bucle principal del juego
        while self.running:
            # Procesamos los eventos
            self.manejar_eventos()
            # Dibujamos en pantalla
            self.draw()
            # Actualizamos la pantalla
            pygame.display.flip()

        # Salimos de pygame cuando termina el bucle
        pygame.quit()
        sys.exit()

    def manejar_eventos(self):

        # Procesamos los eventos (teclado,mouse,cerrar ventana, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill(self.WHITE)
        pygame.draw.line(self.screen,self.GREEN,(20,100),(200,100),5)
        pygame.draw.rect(self.screen,self.BLACK,(75,140,50,50))
        pygame.draw.circle(self.screen,self.BLUE,(100,250),30)
        pygame.draw.circle(self.screen,self.RED,(100,350),30,5)

# Nos aseguramos de que el main se ejecute en este archivo
if __name__ == "__main__":

    # Creamos un objeto de la clase Game
    game = Figuras()

    # Llamamos al método run para que se ejecute el código
    game.run()
