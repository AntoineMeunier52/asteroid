import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill("black")
        updatable.update(dt)

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()
    return


#This line ensures the main() function is only called when this file is run directly;
if __name__ == "__main__":
    main()