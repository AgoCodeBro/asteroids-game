# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *



def main():
    
    # Check for exit
    for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return

    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Making screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Game Loop
    while(True):
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
