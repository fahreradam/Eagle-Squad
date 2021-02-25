import pygame
import player
import objectives
pygame.init()

win_w = 800
win_h = 600
win = pygame.display.set_mode((win_w, win_h))
player = player.Player(400, 300, win)
power = objectives.Power(player.position[0], player.position[1], win)
clock = pygame.time.Clock()

done = False
while not done:
    delta_time = clock.tick() / 1000
    event = pygame.event.poll()
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()

    win.fill((0, 0, 0))
    power.draw()
    player.draw()
    player.move(delta_time)
    power.collide(player.position)
    pygame.display.flip()

    # Exiting
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            done = True
    if event.type == pygame.QUIT:
        done = True
