
import pygame
from constants import *
from player import *
BLACK = (0,0,0)
def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT ))
    clock = pygame.time.Clock()
    my_player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        delta_time = clock.tick(60) / 1000   
        screen.fill(BLACK)
        my_player.update(delta_time)
        my_player.draw(screen)
        pygame.display.flip()
        



if __name__ == "__main__":
    main()
