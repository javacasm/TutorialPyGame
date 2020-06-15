pygame.key.get_pressed() - will get a list of booleans that describes the state of each keyboard key. The value of the key constant (such as pygame.K_TAB) can be used as the index into this giant list. Therefore pygame.key.get_pressed()[pygame.K_TAB] is an expression that is true when the tab key is pressed.

pygame.mouse.get_pos() - returns the coordinates of the mouse cursor. Will return (0, 0) if the mouse hasn't moved over the screen yet.

pygame.mouse.get_pressed() - 
