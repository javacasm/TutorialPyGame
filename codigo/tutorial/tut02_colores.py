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


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ejemplo colores')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.fill(green) # copia screen en la pantalla

    pygame.display.flip()  # 
    