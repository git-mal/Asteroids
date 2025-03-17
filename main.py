import pygame
from circleshape import *
from player import *
from constants import *



def main():
    pygame.init()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable,drawable)

    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    clock = pygame.time.Clock()
    dt = 0
    
    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for object in drawable:
            object.draw(screen)
        #drawable.draw(screen)
        updateable.update(dt)
        pygame.display.flip()
       
        dt = clock.tick(60) / 1000



    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   

if __name__ == "__main__":
    main()