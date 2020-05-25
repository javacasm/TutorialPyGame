import pygame

width = 640
height = 400


# 3 formas de definir los colores
red = pygame.Color('Red')
blue = pygame.Color(0,0,255) # ¿alpha?
green = (0,  255, 0)


screen = pygame.display.set_mode((width, height))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.fill(green) # copia screen en la pantalla

    pygame.display.flip()  # 
    