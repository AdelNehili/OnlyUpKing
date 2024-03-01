class Camera:
    def __init__(self, player, screen_width, screen_height):
        self.player = player
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset_x = 0
        self.offset_y = 0

    def update(self):
        # Center the player in the middle of the screen
        self.offset_x = self.screen_width / 2 - self.player.pos.x
        self.offset_y = self.screen_height / 2 - self.player.pos.y
