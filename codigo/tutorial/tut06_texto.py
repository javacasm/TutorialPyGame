import pygame

width = 640
height = 400


# 3 formas de definir los colores
red = pygame.Color('Red')
agua = pygame.Color('Aqua')
blue = pygame.Color(0,0,255) # ¿alpha?
green = (0,  255, 0)
white = (255,255,255)
black = (0,0,0)

# Sobre los fonts https://www.pygame.org/docs/ref/font.html

"""
pygame.font.Font() espera el path a un fichero con la fuente
pygame.font.Font('fonts/myfont.ttf', size)

pygame.font.SysFont() busca una fuente en sistema con el nombre indicado
pygame.font.SysFont('arial', size)
"""

for font in pygame.font.get_fonts():
    print(font)




screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ejemplo Texto y fonts')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.fill(green) # copia screen en la pantalla

"""
Sobre un font podemos hacer

fornt.set_italic()
fornt.set_bold()
fornt.set_underline()

Podemos saber el tamaño de un texto con
font.size(text) -> (width, height)

Con render generamos una una superfice
surface = font.render(texto,antialias, color)

"""

    pygame.display.flip()  # 
    