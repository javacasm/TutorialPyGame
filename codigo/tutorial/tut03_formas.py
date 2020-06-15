import pygame

width = 800
height = 400


# 3 formas de definir los colores
red = pygame.Color('Red')
agua = pygame.Color('Aqua')
blue = pygame.Color(0,0,255) # ¿alpha?
green = (0,  255, 0)
white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode((width, height))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.fill(green) # copia screen en la pantalla

    pygame.draw.rect(screen, red,(100,100,90,50)) # (x,y,w,h)

    pygame.draw.circle(screen, white, (400,300),100) # (centerX, centerY), radio

    pygame.draw.line(screen, black,(287,95),(595,255),5) # (x1,y1), (x2,y2)

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
    