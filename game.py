import pygame
import sys
import random
from platform_1 import Platform
from player import Player
from camera import Camera

class Game:
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Player(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.platforms = [
            Platform([0, SCREEN_HEIGHT - 0], [SCREEN_WIDTH, 10]),
            Platform([300, 300], [200, 20]),
            Platform([100, 250], [20, 200]),
            Platform([500, 200], [20, 200])
        ]
        self.score = 0
        self.highest_point = SCREEN_HEIGHT // 2
        self.camera = Camera(self.player, SCREEN_WIDTH, SCREEN_HEIGHT)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.player.update(self.platforms)
            self.camera.update()
            self.update_score()
            self.generate_platforms()

            self.screen.fill((255, 255, 255)) #WHITE
            for platform in self.platforms:
                platform.draw(self.screen, self.camera.offset_x, self.camera.offset_y)
            self.player.draw(self.screen, self.camera.offset_x, self.camera.offset_y)

            # Display score
            font = pygame.font.SysFont(None, 55)
            score_text = font.render(f'Score: {self.score}', True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))

            pygame.display.update()
            self.clock.tick(60)


    def update_score(self):
        current_point = self.SCREEN_HEIGHT // 2 - self.player.pos.y
        if current_point > self.highest_point:
            self.highest_point = current_point
            self.score = self.highest_point

    def generate_platforms(self):
        highest_platform = min(self.platforms, key=lambda x: x.pos.y)
        if highest_platform.pos.y > 25:
            new_platform_y = highest_platform.pos.y - random.randint(25, 50)
            new_platform = Platform([random.randint(0, self.SCREEN_WIDTH - 200), new_platform_y], [200, 20])
            self.platforms.append(new_platform)
