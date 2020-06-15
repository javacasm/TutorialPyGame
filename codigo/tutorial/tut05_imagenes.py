"""
Tutorial básico de pyGame

05 - Imágenes

* Cargamos la imagen que genera una superfice pygame.image.load('./images/python-logo.png') devuelve una surface, necesita el path completo
* Hacemos blit a nuestra superficie

Docs: https://www.pygame.org/docs/ref/image.html


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

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ejemplo imágenes')

miImagen = pygame.image.load('./images/python-logo.png')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.fill(white) # copia screen en la pantalla

    screen.blit(miImagen,((width-miImagen.get_width())//2, (height-miImagen.get_height())//2)) # centrado 

    rect = miImagen.get_rect()
    rect.center = (width//2, height//2)

    pygame.display.flip()  # 
    