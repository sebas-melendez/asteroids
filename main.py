
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
BLACK = (0,0,0)
updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updateable, drawable)
Asteroid.containers = (asteroids, updateable, drawable)
AsteroidField.containers =(updateable)
Shot.containers = (shots, updateable ,drawable)
def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT ))
    clock = pygame.time.Clock()
    my_asteroid = AsteroidField()
    my_player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        delta_time = clock.tick(60) / 1000   

        screen.fill(BLACK)

        updateable.update(delta_time)
        for asteroidasos in asteroids:
            
            if asteroidasos.collision(my_player):
                print("Game over!")
                sys.exit(["Game over!"])
            
        for asteroidasos in asteroids:   
            for balitas in shots:
                if asteroidasos.collision(balitas):
                    asteroidasos.split()

        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        

  

if __name__ == "__main__":
    main()
