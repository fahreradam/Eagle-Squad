import pygame
import player
pygame.init()

win_w = 800
win_h = 600
win = pygame.display.set_mode((win_w, win_h))
player = player.Player(400, 300, win)
clock = pygame.time.Clock()

done = False
while not done:
    delta_time = clock.tick() / 1000
    event = pygame.event.poll()
    keys = pygame.key.get_pressed()

    player.draw()
    player.move(delta_time)

    # Exiting
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            done = True
    if event.type == pygame.QUIT:
        done = True
