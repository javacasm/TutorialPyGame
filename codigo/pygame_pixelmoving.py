# movingPixel from https://lorenzod8n.wordpress.com/2007/12/16/pygame-tutorial-5-pixels/

import pygame

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class MovingPixel:
    """ A moving pixel class """

    def __init__(self, x, y):
        """ Creates a moving pixel. """
        self.x = x
        self.y = y
        self.hdir = 0
        self.vdir = -1

    def direction(self, dir):
        """ Change the pixels direction """
        self.hdir, self.vdir = dir

    def move(self):
        """ Move the pixel """
        self.x += self.hdir
        self.y += self.vdir

    def draw(self, surface):
        surface.set_at((self.x, self.y), (255, 255, 255))


width = 640
height = 400

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

# Create the moving pixel
pix = MovingPixel(width//2, height//2)

while running:
    pix.move()

    if pix.x <= 0 or pix.x >= width or pix.y <= 0 or pix.y >= height:
        print("Crash!!!")
        running = False

    screen.fill((0, 0, 0))
    pix.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pix.direction(UP)
            elif event.key == pygame.K_DOWN:
                pix.direction(DOWN)
            elif event.key == pygame.K_RIGHT:
                pix.direction(RIGHT)
            elif event.key == pygame.K_LEFT:
                pix.direction(LEFT)
    pygame.display.flip()
    clock.tick(120)
