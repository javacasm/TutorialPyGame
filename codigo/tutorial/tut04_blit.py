"""
Tutorial básico de pyGame

04 - Superfices y blit

Podemos utilizar varias superfices 

miSuperfice = Surface((width, height))

surface.blit(miSuperficie, (xDestino, yDestino))

Podemos usar transparencias surface = pygame.Surface((100, 100), pygame.SRCALPHA)

Docs: https://www.pygame.org/docs/ref/surface.html



CC by SA @javacasm
Junio 2020

"""
import pygame

width = 640
height = 400


# 3 formas de definir los colores
red = pygame.Color('Red')
blue = pygame.Color(0,0,255) # ¿alpha?
green = (0,  255, 0)
white = (255,255,255)
black = (0,0,0)

pygame.init() # Inicializa el entorno de pygame

miSuperfice = pygame.Surface((300,300)) # (width, height)
miSuperfice.fill(blue)



screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ejemplo surfaces')
 
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.fill(green) # copia screen en la pantalla

    screen.blit(miSuperfice,(150,100))

    pygame.display.flip()  # 
    
