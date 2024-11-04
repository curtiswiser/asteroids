import pygame
from constants import *

def main(): 
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen_color = (0,0,0)
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    #infinate gaming loop
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(screen_color)
        pygame.display.flip()
        
        

if __name__== "__main__":
    main()
    