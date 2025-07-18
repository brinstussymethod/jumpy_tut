"""
# inside Platform.update()
#check if platform has gone off the screen
if self.rect.top > SCREEN_HEIGHT:
    self.kill()


#generate platforms
if len(platform_group) < MAX_PLATFORMS:
    p_w = random.randint(40, 60)
    p_x = random.randint(0, SCREEN_WIDTH - p_w)
    p_y = platform.rect.y - random.randint(80, 120)
    platform = Platform(p_x, p_y, p_w)
    platform_group.add(platform)

#create starting platform
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100)
platform_group.add(platform)


remove:
for p in range(MAX_PLATFORMS):
    ...



"""