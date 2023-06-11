# pygame para el juego
import pygame
import Personaje
# Reloj para frames
RELOJ = pygame.time.Clock()

# color para el fondo en RGB
background_color = (0, 0, 0)

# creamos una figura en el centro de la pantalla con dimensiones 100px, velocidad 10 (sin uso aún)
personaje = Personaje.Personaje( Personaje.POS_X,
                                Personaje.POS_Y,
                                Personaje.velocidadDesplazamiento,
                                (255,255,255),
                                20)

# Titulo en ventana
pygame.display.set_caption('Demo Juego')

# Flag de mantenerse activo
running = True
# se mantiene ventana activa con un flag
while running:
    # llenar el fondo
    Personaje.screen.fill(background_color)
    # eventos durante la actividad
    for event in pygame.event.get():
        # deteccion de teclas
        if event.type == pygame.KEYDOWN:
            match (event.key):
                case (pygame.K_w) | (pygame.K_UP):
                    personaje.up()
                case (pygame.K_a) | (pygame.K_LEFT):
                    personaje.left()
                case (pygame.K_s) | (pygame.K_DOWN):
                    personaje.down()
                case (pygame.K_d) | (pygame.K_RIGHT):
                    personaje.right()
                case (pygame.K_SPACE):
                    personaje.salto()
                case (pygame.K_h) | (pygame.K_ESCAPE):
                    # Cerrar
                    running = False
        # detecta cierre de ventana
        if event.type == pygame.QUIT:
            running = False

    print(personaje.x , " <x,y> " , personaje.y)
    
    # mandamos al personaje creado a la pantalla
    personaje.render()
    # se lo manda a la ventana
    pygame.display.flip()
    pygame.display.update()
    RELOJ.tick(10)
