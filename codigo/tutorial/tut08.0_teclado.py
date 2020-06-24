"""
Tutorial básico de pyGame

08 - Eventos de teclado:

Eventos y sus propiedades

QUIT              none
ACTIVEEVENT       gain, state
KEYDOWN           key, mod, unicode, scancode
KEYUP             key, mod
MOUSEMOTION       pos, rel, buttons
MOUSEBUTTONUP     pos, button
MOUSEBUTTONDOWN   pos, button
JOYAXISMOTION     joy, axis, value
JOYBALLMOTION     joy, ball, rel
JOYHATMOTION      joy, hat, value
JOYBUTTONUP       joy, button
JOYBUTTONDOWN     joy, button
VIDEORESIZE       size, w, h
VIDEOEXPOSE       none
USEREVENT         code

Eventos de teclado:

Propiedad key 
    pygame.K_q ...
    pygame.K_LEFT ...

Docs: 
* Eentos https://www.pygame.org/docs/ref/event.html


CC by SA @javacasm
Junio 2020

"""

import pygame

width = 640
height = 400


# 3 formas de definir los colores
red = pygame.Color('Red')
cyan = pygame.Color('cyan')
blue = pygame.Color(0,0,255) # ¿alpha?
green = (0,  255, 0)
white = (255,255,255)
black = (0,0,0)

pygame.init() # Inicializa el entorno de pygame

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ejemplo colores')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.KEYDOWN:
            print('Teca pulsada: '+event.unicode)

            if event.key == pygame.K_q:
                running == False

            if event.key == pygame.K_o or event.key == pygame.K_LEFT:
                print('Movmiento izda')

            if event.key == pygame.K_p or event.key == pygame.K_RIGHT:
                print('Movmiento drcha')                

            if event.key == pygame.K_a or event.key == pygame.K_UP:
                print('Movmiento arriba')

            if event.key == pygame.K_z or event.key == pygame.K_DOWN:
                print('Movmiento abajo')                                

        if event.type == pygame.KEYUP:
            print('Teca suelta')
             
             
    
    screen.fill(green) # copia screen en la pantalla

    pygame.display.flip()  # 
    