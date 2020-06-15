"""
Tutorial básico de pyGame

01 - Ejemplo base: 
* pygame.init() # Inicializa el entorno de pygame
* Mostramos una venana de tamaño width, height 
* Con título  display.set_caption('Título')
* Comprueba los eventos 
    * Responde al evento de cierre
* display.flip() para actualizar la ventana 


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
    
    pygame.display.flip()
    