import pygame
from constants import *
from player import Player

def main(): 
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

    #create groups: 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    updatable.add(player)
    drawable.add(player)

    #infinate gaming loop
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        milliseconds = clock.tick(60)#this sets the frame rate to 60 fps
        dt = milliseconds/1000 #converts the value to seconds. used to align the functions to the frame rate

        for obj in updatable:
            obj.update(dt = dt)
        screen.fill("black")#clear screen

        for obj in drawable:
            obj.draw(screen = screen)
      
        pygame.display.flip()

if __name__== "__main__":
    main()
    