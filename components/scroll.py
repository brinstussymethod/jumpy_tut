"""
SCROLL_THRESH = 200
scroll = 0
bg_scroll = 0


def draw_bg(bg_scroll):
	screen.blit(bg_image, (0, 0 + bg_scroll))
	screen.blit(bg_image, (0, -600 + bg_scroll))

#check if the player has bounced to the top of the screen
if self.rect.top <= SCROLL_THRESH:
	#if player is jumping
	if self.vel_y < 0:
		scroll = -dy


scroll = jumpy.move()
bg_scroll += scroll
if bg_scroll >= 600:
	bg_scroll = 0
draw_bg(bg_scroll)

pygame.draw.line(screen, WHITE, (0, SCROLL_THRESH), (SCREEN_WIDTH, SCROLL_THRESH))
"""