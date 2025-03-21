import pygame
import sys
from asteroidfield import *
from asteroid import *
from circleshape import *
from player import *
from constants import *
from shot import *


def main():
    pygame.init()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable,drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (shots ,updateable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    
    #test var
    fps = 0
    test_ticker = 0 
    #test var
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        
        for object in drawable:
            object.draw(screen)
        
        updateable.update(dt)

        for roid in asteroids:
            if roid.collision_check(player) == True:
                print('Game Over!')
                clock.tick(1)
                pygame.QUIT
                sys.exit()

        pygame.display.flip()
        #test code
        fps = pygame.time.Clock.get_fps(clock)
        test_ticker += 1
        if test_ticker % 60 == 0:
            print(f"FPS: {round(fps,2)}")
            print(f"shoot cooldown is {round(player.shoot_cd_timer,2)} seconds")
        #test code
        dt = clock.tick(60) / 1000



    
   
   

   
   

   
   
   
   
   
   
   
   
   
   
   
   
   
   

if __name__ == "__main__":
    main()