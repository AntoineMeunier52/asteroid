import pygame
from constants import *

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill("black")

        pygame.display.flip()

    pygame.quit()
    return


#This line ensures the main() function is only called when this file is run directly;
if __name__ == "__main__":
    main()