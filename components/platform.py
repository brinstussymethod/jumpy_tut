"""
import random
platform_image = pygame.image.load('assets/wood.png').convert_alpha()
MAX_PLATFORMS = 10

class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y, width):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(platform_image, (width, 10))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

platform_group = pygame.sprite.Group()
for p in range(MAX_PLATFORMS):
	p_w = random.randint(40, 60)
	p_x = random.randint(0, SCREEN_WIDTH - p_w)
	p_y = p * random.randint(80, 120)
	platform = Platform(p_x, p_y, p_w)
	platform_group.add(platform)

for platform in platform_group:
	if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
		if self.rect.bottom < platform.rect.centery:
			if self.vel_y > 0:
				self.rect.bottom = platform.rect.top
				dy = 0
				self.vel_y = -20

platform_group.draw(screen)


"""