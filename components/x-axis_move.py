"""
everything you need to add left and right movement

clock = pygame.time.Clock()
FPS = 60

Do not forget to add this in your dunder method
self.flip = False

def move(self):
    #reset variables
    dx = 0
    dy = 0

    #process keypresses
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        dx = -10
        self.flip = True
    if key[pygame.K_d]:
        dx = 10
        self.flip = False

    #ensure player doesn't go off the edge of the screen
    if self.rect.left + dx < 0:
        dx = -self.rect.left
    if self.rect.right + dx > SCREEN_WIDTH:
        dx = SCREEN_WIDTH - self.rect.right

    #update rectangle position
    self.rect.x += dx
    self.rect.y += dy

clock.tick(FPS)
jumpy.move()



"""