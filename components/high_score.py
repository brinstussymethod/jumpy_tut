"""
if os.path.exists('score.txt'):
    with open('score.txt', 'r') as file:
        high_score = int(file.read())
else:
    high_score = 0

if scroll > 0:
    score += scroll

pygame.draw.line(screen, WHITE, (0, score - high_score + SCROLL_THRESH), (SCREEN_WIDTH, score - high_score + SCROLL_THRESH), 3)
draw_text('HIGH SCORE', font_small, WHITE, SCREEN_WIDTH - 130, score - high_score + SCROLL_THRESH)


if score > high_score:
    high_score = score
    with open('score.txt', 'w') as file:
        file.write(str(high_score))

if score > high_score:
    high_score = score
    with open('score.txt', 'w') as file:
        file.write(str(high_score))



"""