# https://nerdparadise.com/programming/pygame/part1
https://www.geeksforgeeks.org/python-moving-an-object-in-pygame/

# import pygame module in this program  
import pygame 
  
# activate the pygame library .   
# initiate pygame and give permission   
# to use pygame's functionality.   
pygame.init() 
  
# create the display surface object   
# of specific dimension..e(500, 500).   
win = pygame.display.set_mode((500, 500)) 
  
# set the pygame window name  
pygame.display.set_caption("Moving rectangle") 
  
# object current co-ordinates  
x = 200
y = 200
  
# dimensions of the object  
width = 20
height = 20
  
# velocity / speed of movement 
vel = 10
  
# Indicates pygame is running 
run = True
  
# infinite loop  
while run: 
    # creates time delay of 10ms  
    pygame.time.delay(10) 
      
    # iterate over the list of Event objects   
    # that was returned by pygame.event.get() method.   
    for event in pygame.event.get(): 
          
        # if event object type is QUIT   
        # then quitting the pygame   
        # and program both.   
        if event.type == pygame.QUIT: 
              
            # it will make exit the while loop  
            run = False
    # stores keys pressed  
    keys = pygame.key.get_pressed() 
      
    # if left arrow key is pressed 
    if keys[pygame.K_LEFT] and x>0: 
          
        # decrement in x co-ordinate 
        x -= vel 
          
    # if left arrow key is pressed 
    if keys[pygame.K_RIGHT] and x<500-width: 
          
        # increment in x co-ordinate 
        x += vel 
         
    # if left arrow key is pressed    
    if keys[pygame.K_UP] and y>0: 
          
        # decrement in y co-ordinate 
        y -= vel 
          
    # if left arrow key is pressed    
    if keys[pygame.K_DOWN] and y<500-height: 
        # increment in y co-ordinate 
        y += vel 
         
              
    # completely fill the surface object   
    # with black colour   
    win.fill((0, 0, 0)) 
      
    # drawing object on screen which is rectangle here  
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) 
      
    # it refreshes the window 
    pygame.display.update()  
  
# closes the pygame window  
pygame.quit() 


o 


import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        
        screen.fill((0, 0, 0))
        
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()
