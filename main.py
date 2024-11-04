import pygame
from constants import *

def main(): 
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #infinate gaming loop
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        milliseconds = clock.tick(60)
        dt = milliseconds/1000 #converts the value to seconds
        

if __name__== "__main__":
    main()
    