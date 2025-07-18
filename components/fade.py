"""
fade_counter = 0
BLACK = (0, 0, 0)


if fade_counter < SCREEN_WIDTH:
    fade_counter += 5
    for y in range(0, 6, 2):
        pygame.draw.rect(screen, BLACK, (0, y * 100, fade_counter, 100))
        pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - fade_counter, (y + 1) * 100, SCREEN_WIDTH, 100))
fade_counter = 0

"""