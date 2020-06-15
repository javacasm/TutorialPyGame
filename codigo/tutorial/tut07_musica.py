"""
Tutorial básico de pyGame

07 - Ejemplo musica: 
* pygame.mixer.music.load(fichero) # carga el fichero
* pygame.mixer.music.play() # reproduce
* pygame.mixer.music.play(repeticion, segundoInicio) # repeticion = -1 bucle infinito
* pygame.mixer.music.set_volume(volumen ) # volumen entre 0 y 1.0
* pygame.mixer.music..stop() # detiene
* pygame.mixer.music..pause()  # para 
* plpygame.mixer.music.ay.unpause()  # continua
* play.rewind()  # reinicia
* play.fadeout( milisegundos hasta apagarse) # apaga poco a poco


Docs sobre mixer.music: https://www.pygame.org/docs/ref/music.html

mp3: fortunate note from Youtube free music library

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

pygame.mixer.music.load('./music/Fortunate_Note.mp3') # cargamos el fichero
pygame.mixer.music.set_volume(0.5 ) # volumen entre 0 y 1.0
pygame.mixer.music.play()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.fill(green) # copia screen en la pantalla

    pygame.display.flip()  # 
    