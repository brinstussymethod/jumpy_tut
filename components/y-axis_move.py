"""
everything you need to add up and down movement

GRAVITY = 1

self.vel_y = 0

self.vel_y += GRAVITY
dy += self.vel_y

if self.rect.bottom + dy > SCREEN_HEIGHT:
	dy = 0
	self.vel_y = -20

"""