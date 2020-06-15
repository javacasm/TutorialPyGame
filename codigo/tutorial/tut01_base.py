import pygame

width = 640
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ejemplo base')
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    pygame.display.flip()
    