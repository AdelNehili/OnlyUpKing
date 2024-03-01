import pygame

class Player:
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT):
        self.size = 50
        self.pos = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.velocity = pygame.Vector2(5, 0)
        self.max_jump_power = 50
        self.jump_velocity = self.max_jump_power
        self.gravity = 0.5
        self.jump = False
        self.color = (0, 0, 255) #BLUE

    def update(self, platforms):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pos.x -= self.velocity.x
        if keys[pygame.K_RIGHT]:
            self.pos.x += self.velocity.x

        if not self.jump:
            if keys[pygame.K_SPACE]:
                self.jump = True
        else:
            self.pos.y -= self.jump_velocity
            self.jump_velocity -= self.gravity
            if self.check_collision(platforms):
                self.jump = False
                self.jump_velocity = 10

    def draw(self, screen, offset_x, offset_y):
        pygame.draw.rect(screen, self.color, (self.pos.x + offset_x, self.pos.y + offset_y, self.size, self.size))

    def check_collision(self, platforms):
        p_rect = pygame.Rect(self.pos.x, self.pos.y, self.size, self.size)
        for platform in platforms:
            platform_rect = pygame.Rect(platform.pos.x, platform.pos.y, platform.size.x, platform.size.y)
            if p_rect.colliderect(platform_rect):
                if self.pos.y - self.jump_velocity < platform_rect.top:
                    return True
        return False
