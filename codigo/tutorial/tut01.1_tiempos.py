"""
Tutorial básico de pyGame

00 - Medida de tiempos
* time.get_ticks() tiempo transcurrido desde que se llamó a pygmae.init() en milisegundos
* Podemos ver el tiempo transcurrido restando el número de ticks entre los 2 sucesos


Docs: https://www.pygame.org/docs/ref/display.html

display.flip: Actualiza toda la surface a pantalla
display.update(rect): Actualiza un rectángulo  (¿sin argumentos actualiza todo?)

CC by SA @javacasm
Junio 2020

"""

import pygame

width = 640
height = 400

pygame.init() # Inicializa el entorno de pygame

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ejemplo base')
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    print(pygame.time.get_ticks())

    pygame.display.flip()