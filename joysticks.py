import pygame

pygame.joystick.init()
print('Hay {} joysticks'.format(pygame.joystick.get_count()))

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

for js in joysticks:
    print(js.get_name())