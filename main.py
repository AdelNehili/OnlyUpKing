import pygame
from game import Game


if __name__ == "__main__":
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255) #BLUE
    PLATFORM_COLOR = (0, 255, 0) #GREEN
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.run()
