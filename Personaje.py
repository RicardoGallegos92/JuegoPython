import pygame

# dimensiones pantalla (width,height)
alto = 800
ancho = 600
velocidadDesplazamiento = 10
GRAVEDAD = 10

POS_X = ancho//2
POS_Y = alto//2

# Defininmos clase personaje con sus atributos

screen = pygame.display.set_mode((alto, ancho))

class Personaje():
    def __init__(self, pos_X, pos_Y, velocidad, color, tamano):
        self.x = pos_X
        self.y = pos_Y
        self.velocidad = velocidad
        self.color = color
        self.tamano = tamano
#       pygame.Rect( pos_X, pos_Y, ancho, alto )
#        self.caja1 = pygame.Rect(self.x, self.y, self.tamano, self.tamano*2)
#        self.caja2 = pygame.Rect(0,0, tamano//2, tamano)
#        self.caja2.center = self.caja1.center

    def render(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.tamano, self.tamano*1.5))
#        pygame.draw.rect(screen, self.color, ((20,20, self.tamano//2, self.tamano)))
#        pygame.draw.rect(screen, self.color, self.caja1)
#        pygame.draw.rect(screen, (125,125,125), self.caja2)
    def up(self):
        self.y = self.y - self.velocidad

    def left(self):
        self.x = self.x - self.velocidad

    def down(self):
        self.y = self.y + self.velocidad

    def right(self):
        self.x = self.x + self.velocidad

    def salto(self):
        print("Saltanding")
            