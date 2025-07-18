"""
This is all the components you need to draw a player on the screen

WHITE = (255, 255, 255)

jumpy_image = pygame.image.load('assets/jump.png').convert_alpha()

class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(jumpy_image, (45, 45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x - 12, self.rect.y - 5))
        pygame.draw.rect(screen, WHITE, self.rect, 2)

jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

jumpy.draw()

"""