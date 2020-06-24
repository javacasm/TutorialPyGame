"""
Tutorial básico de pyGame

08 - Eventos de teclado:

KEYDOWN           key, mod, unicode, scancode
KEYUP             key, mod


Eventos de teclado:

Propiedades:
* key 
    pygame.K_q ...
    pygame.K_LEFT ...
* unicode
* mod son bits que pueden estar activos al mismo tiempo. Lo comprobamos con OR de la constate
    KMOD_NONE     no modifier keys pressed
    KMOD_LSHIFT   left shift
    KMOD_RSHIFT   right shift
    KMOD_SHIFT    left shift or right shift or both
    KMOD_LCTRL    left control
    KMOD_RCTRL    right control
    KMOD_CTRL     left control or right control or both
    KMOD_LALT     left alt
    KMOD_RALT     right alt
    KMOD_ALT      left alt or right alt or both
    KMOD_LMETA    left meta
    KMOD_RMETA    right meta
    KMOD_META     left meta or right meta or both
    KMOD_CAPS     caps lock
    KMOD_NUM      num lock
    KMOD_MODE     AltGr

Docs: 
* Eentos https://www.pygame.org/docs/ref/event.html
* Keys https://www.pygame.org/docs/ref/key.html


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

            if event.mod == pygame.KMOD_NONE:
                print('No modifier keys were in a pressed state when this '
                    'event occurred.')
            else:
                if event.mod & pygame.KMOD_LSHIFT:
                    print('Left shift was in a pressed state when this event '
                        'occurred.')
                if event.mod & pygame.KMOD_RSHIFT:
                    print('Right shift was in a pressed state when this event '
                        'occurred.')
                if event.mod & pygame.KMOD_SHIFT:
                    print('Left shift or right shift or both were in a '
                        'pressed state when this event occurred.')

        if event.type == pygame.KEYUP:
            print('Teca suelta')
             
             
    
    screen.fill(green) # copia screen en la pantalla

    pygame.display.flip()  # 
    