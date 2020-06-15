"""
Tutorial básico de pyGame

03 - Formas, líneas y polígonos

* draw.----(surface, color, parámetros)
    * Rectángulo: draw.rect(screen,color,(x,y,w,h))
    * Círculo: draw.circle(screen,color,(centerX, centerY), radio)
    * Línea: draw.line(screen,color, (x1,y1), (x2,y2), grosor)
    * Polígono: draw.polygon(screen,color,((x1,y1), (x2,y2), ....))
* Rect: tiene una propiedad center que podemos usar para centrar en pantalla

Docs sobre draw https://www.pygame.org/docs/ref/draw.html

CC by SA @javacasm
Junio 2020

"""

import pygame

width = 800
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

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.fill(green) # copia screen en la pantalla

    pygame.draw.rect(screen, red,(100,100,90,50)) # (x,y,w,h)

    pygame.draw.circle(screen, white, (400,300),100) # (centerX, centerY), radio

    pygame.draw.line(screen, black,(287,95),(595,255),5) # (x1,y1), (x2,y2), grosor

    pygame.draw.polygon(screen, blue,(
                (500,200),
                (600,100),
                (700,200)
    ))

    pygame.draw.polygon(screen, red,(
                (50,200),
                (0,150),
                (100,100),
                (200,150),
                (150,200)
    ))

    pygame.display.flip()  # ¿diferencia con update?
    