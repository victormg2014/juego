import pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
MAGENTA = (255, 0, 255)
FPS = 60
#nombre= 'fondo.jpg'

class Cuadrado:
    def __init__(self, x, y, lado, color, fondo):
        self.x = x
        self.y = y
        self.color = color
        self.fondo = fondo
        self.lado = lado
        self.rect = pygame.Rect(self.x,
                                self.y,
                                self.lado,
                                self.lado)

    def __pinta(self, pantalla, color):
        'Realiza el dibujo efectivo'
        pygame.draw.rect(pantalla, color, self.rect, 0)

    def pinta(self, pantalla):
        'Pinta el cuadrado con el color propio'
        self.__pinta(pantalla, self.color)

    def borra(self, pantalla):
        'Borra el cuadrado'
        # Realmente lo pinta con el color de fondo
        self.__pinta(pantalla, self.fondo)

    def colisiona_con(self, cuadrado2):
        'Comprueba la colisión con otro cuadrado'
        return self.rect.colliderect(cuadrado2.rect)

    def mover(self, avance_x, avance_y):
        'avance del cuadrado en un cuadro (frame)'
        self.rect.move_ip(avance_x, avance_y)

    def mover_p(self, pantalla, avance_x, avance_y):
        'avance del cuadrado en un cuadro, con refresco de pantalla'
        cuadrado.borra(pantalla)
        rect_inicial = cuadrado.rect.copy()
        cuadrado.mover(avance_x, avance_y)
        rect_final = cuadrado.rect.copy()
        cuadrado.pinta(pantalla)
        pygame.display.update(rect_final.union(rect_inicial))


# inicializamos pygame
pygame.init()

# definición de la pantalla
pantalla = pygame.display.set_mode((640, 480))
#pantalla.fill(NEGRO)
fondo = pygame.image.load("fondo.jpg").convert()
pantalla.blit(fondo, (0, 0))

cuadrado = Cuadrado(50, 50, 35, BLANCO, NEGRO)
cuadrado2 = Cuadrado(540, 50, 35, MAGENTA, NEGRO)
cuadrado.pinta(pantalla)
cuadrado2.pinta(pantalla)
pygame.display.update()

# reloj de control de refresco
clock = pygame.time.Clock()

while not cuadrado.colisiona_con(cuadrado2):
    # pausa hasta el siguiente "tick" de reloj
    #clock.tick(FPS)

    # detección de evento QUIT (aspa)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Movimiento
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cuadrado.mover_p(pantalla, -20, 0)

            if event.key == pygame.K_RIGHT:
                cuadrado.mover_p(pantalla, 20, 0)

            if event.key == pygame.K_UP:
                cuadrado.mover_p(pantalla, 0, -20)

            if event.key == pygame.K_DOWN:
                cuadrado.mover_p(pantalla, 0, 20)

print("Has ganado")

pygame.time.delay(3000)
pygame.quit()
