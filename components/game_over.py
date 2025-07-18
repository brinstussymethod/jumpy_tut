"""
game_over = False

score = 0

font_small = pygame.font.SysFont('Lucida Sans', 20)
font_big = pygame.font.SysFont('Lucida Sans', 24)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#check game over
if jumpy.rect.top > SCREEN_HEIGHT:
    game_over = True

if key[pygame.K_SPACE]:
    #reset variables
    game_over = False
    score = 0
    scroll = 0
    jumpy.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
    platform_group.empty()
    platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100)
    platform_group.add(platform)


draw_text('GAME OVER!', font_big, WHITE, 130, 200)
draw_text('SCORE: ' + str(score), font_big, WHITE, 130, 250)
draw_text('PRESS SPACE TO PLAY AGAIN', font_big, WHITE, 40, 300)]

wrap mainloop in between these

if game_over == False:
    ...
else:
    ...


REMOVE COLLISION WITH THE GROUND

"""