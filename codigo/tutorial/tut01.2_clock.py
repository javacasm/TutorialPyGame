"""
¿A qué velocidad se ejecuta?
¿Necesitamos que sea tan rápido?

https://nerdparadise.com/programming/pygame/part1
"""
clock = pygame.time.Clock()

while not done:
	    pygame.display.flip()

		# will block execution until 1/60 seconds have passed
		# since the previous time clock.tick was called.
        clock.tick(60)
