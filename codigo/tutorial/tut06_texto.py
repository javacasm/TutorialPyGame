"""
Tutorial básico de pyGame

06 - Texto y Fonts

Creación de font:
Font de usuario
* pygame.font.Font('fonts/myfont.ttf', size)  espera el path a un fichero con la fuente
Fonts del sistema
* pygame.font.SysFont('arial', size) busca una fuente en sistema con el nombre indicado

Sobre un font podemos hacer

* fornt.set_italic()
* fornt.set_bold()
* fornt.set_underline()

Podemos saber el tamaño de un texto con
font.size(text) -> (width, height)

Con render generamos en una superfice
surface = font.render(texto, antialias, color)

Docs sobre fonts: https://www.pygame.org/docs/ref/font.html

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

for font in pygame.font.get_fonts():
    print(font)


sysFont = pygame.sysfont.SysFont('freemono',20,bold = True)
miFont = pygame.font.Font('./fonts/Gamer.ttf',100)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ejemplo Texto y fonts')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.fill(cyan) # copia screen en la pantalla

    textSurface = sysFont.render('Una prueba', True, black)
    text2Surface = miFont.render('MiFont',True,blue)
    
    rect = textSurface.get_rect()
    rect.center = (width//2, height//2)

    screen.blit(textSurface, rect)

    rect2 = text2Surface.get_rect()
    rect2.center = (width//2, height//2 + 100)

    screen.blit(text2Surface, rect2)

    pygame.display.flip()  # 
    