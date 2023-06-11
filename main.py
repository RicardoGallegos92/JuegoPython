# pygame para el juego
import pygame

# color para el fondo en RGB
background_color = (0, 0, 0)

# dimensiones pantalla (width,height)
alto = 800
ancho = 600

pygame.init()
screen = pygame.display.set_mode((alto, ancho))

# Defininmos clase personaje con sus atributos
class Personaje():
    def __init__(self, ejeX, ejeY, velocidad, color, tamano):
        self.x = ejeX
        self.y = ejeY
        self.velocidad = velocidad
        self.color = color
        self.tamano = tamano

    def render(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.tamano, self.tamano))

# creamos una figura en el centro de la pantalla con dimensiones 100px, velocidad 10 (sin uso aún)
personaje = Personaje( ancho // 2 , alto // 2, 0.1, (255,255,255), 100)

# Titulo en ventana
pygame.display.set_caption('Demo Juego')

# Flag de mantenerse activo
running = True
# se mantiene ventana activa con un flag
while running:
    # llenar el fondo
    screen.fill(background_color)
    # mandamos al personaje creado a la pantalla
    personaje.render()
    # se lo manda a la ventana
    pygame.display.flip()
    # eventos durante la actividad
    for event in pygame.event.get():
        # deteccion de teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                # elegimos cerrar con H sin ninguna buena razón
                running = False
        # detecta cierre de ventana
        if event.type == pygame.QUIT:
            running = False