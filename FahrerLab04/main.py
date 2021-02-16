# Adam Fahrer
# Lab 04
# 2/10/2021

import pygame
import random

pygame.init()

win_w = 640
win_h = 480
win = pygame.display.set_mode((win_w, win_h))

clock = pygame.time.Clock()
neg_x = 1
neg_y = 1

circ_x = win_w / 2
circ_y = win_h / 2
time = 0
color = (0, 0, 255)
screen_01 = True
screen_02 = False
screen_03 = False
screen_04 = False
move = False
vibrate = False
run = True
direction = False
while run:
    dt = clock.tick() / 1000
    event = pygame.event.poll()
    keys = pygame.key.get_pressed()
    mPos = pygame.mouse.get_pos()
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    if keys[pygame.K_SPACE]:
        direction = True
        move = True
    if direction:
        neg_x = random.choice([-1, 1]) * neg_x
        neg_y = random.choice([-1, 1]) * neg_x
        direction = False

    # Movement
    if move and not vibrate:
        circ_x -= 1000 * dt * neg_x
        circ_y += 1000 * dt * neg_y

    # Drawing
    blue_c = pygame.draw.circle(win, color, (int(circ_x), int(circ_y)), 50)
    pygame.display.flip()

    if screen_01:
        win.fill((255, 255, 255))
        pygame.draw.rect(win, (0, 0, 0), (630, int(win_h / 3), 10, 160))

        # Side Walls
        if circ_x - 50 <= 0:
            circ_x = 50
            neg_x = -neg_x
        if circ_y + 50 >= win_h:
            circ_y = win_h - 50
            neg_y = -neg_y
        if circ_x + 50 >= win_w:
            screen_04 = True
            circ_x = 51
            screen_01 = False
        if circ_y - 50 <= 0:
            screen_02 = True
            circ_y = win_h - 51
            screen_01 = False
        if 630 <= circ_x + 50 <= 640 and win_h / 3 <= circ_y <= win_h / 3 + 160:
            circ_x = win_w - 60
            neg_x = -neg_x

        # Restarting if the red circle is hit
        if vibrate:
            time += dt
            circ_x += random.uniform(0.1, 0.2)
            circ_x -= random.uniform(0.1, 0.2)
            if int(time) == 2:
                circ_x = win_w / 2
                circ_y = win_h / 2
                time = 0
                color = (red, green, blue)
                vibrate = False

    if screen_02:
        win.fill((255, 255, 255))
        left = pygame.draw.rect(win, (0, 0, 0), (int(win_w / 4), int(win_h / 3), 15, 160))
        middle = pygame.draw.rect(win, (0, 0, 0), (int(win_w * 2 / 4), int(win_h / 3), 15, 160))
        right = pygame.draw.rect(win, (0, 0, 0), (int(win_w * 3 / 4), int(win_h / 3), 15, 160))
        pygame.draw.rect(win, (0, 0, 0), (win_w - 10, 0, 10, 100))
        pygame.draw.rect(win, (0, 0, 0), (630, int(win_h * 2 / 3), 10, 100))

        # Left Block
        if win_w / 4 <= circ_x + 50 <= win_w / 4 + 15 and win_h / 3 <= circ_y <= win_h / 3 + 160:
            circ_x = win_w / 4 - 50
            neg_x = -neg_x
        if win_w / 4 <= circ_x - 50 <= win_w / 4 + 15 and win_h / 3 <= circ_y <= win_h / 3 + 160:
            circ_x = win_w / 4 + 65
            neg_x = -neg_x
        # if win_w / 4 <= circ_x <= win_w / 4 + 15 and win_h / 3 <= circ_y + 50 <= win_h / 3 + 160:
        #     circ_y = win_h / 3 - 50
        #     neg_y = -neg_y
        # if win_w / 4 <= circ_x <= win_w / 4 + 15 and win_h / 3 <= circ_y - 50 <= win_h / 3 + 160:
        #     circ_y = win_h / 3 + 210
        #     neg_y = -neg_y
        if blue_c.colliderect(left):
            if circ_y >= win_h / 3 + 160 and not circ_y <= win_h / 3 + 130:
                circ_y = win_h / 3 + 210
                neg_y = -neg_y
            if circ_y <= win_h / 3 and not circ_y >= win_h / 3 + 10:
                circ_y = win_h / 3 - 50
                neg_y = -neg_y

        # Middle Block
        if win_w * 2 / 4 <= circ_x + 50 <= win_w * 2 / 4 + 15 and win_h / 3 <= circ_y <= win_h / 3 + 160:
            circ_x = win_w * 2 / 4 - 50
            neg_x = -neg_x
        if win_w * 2 / 4 <= circ_x - 50 <= win_w * 2 / 4 + 15 and win_h / 3 <= circ_y <= win_h / 3 + 160:
            circ_x = win_w * 2 / 4 + 65
            neg_x = -neg_x
        # if win_w * 2 / 4 <= circ_x <= win_w * 2 / 4 + 15 and win_h / 3 <= circ_y + 50 <= win_h / 3 + 160:
        #     circ_y = win_h / 3 - 50
        #     neg_y = -neg_y
        # if win_w * 2 / 4 <= circ_x <= win_w * 2 / 4 + 15 and win_h / 3 <= circ_y - 50 <= win_h / 3 + 160:
        #     circ_y = win_h / 3 + 210
        #     neg_y = -neg_y
        if blue_c.colliderect(middle):
            if circ_y >= win_h / 3 + 160 and not circ_y <= win_h / 3 + 130:
                circ_y = win_h / 3 + 210
                neg_y = -neg_y
            if circ_y <= win_h / 3 and not circ_y >= win_h / 3 + 10:
                circ_y = win_h / 3 - 50
                neg_y = -neg_y

        # Right Block
        if win_w * 3 / 4 <= circ_x + 50 <= win_w * 3 / 4 + 15 and win_h / 3 <= circ_y <= win_h / 3 + 160:
            circ_x = win_w * 3 / 4 - 50
            neg_x = -neg_x
        if win_w * 3 / 4 <= circ_x - 50 <= win_w * 3 / 4 + 15 and win_h / 3 <= circ_y <= win_h / 3 + 160:
            circ_x = win_w * 3 / 4 + 65
            neg_x = -neg_x
        # if win_w * 3 / 4 <= circ_x <= win_w * 3 / 4 + 15 and win_h / 3 <= circ_y + 50 <= win_h / 3 + 160:
        #     circ_y = win_h / 3 - 50
        #     neg_y = -neg_y
        # if win_w * 3 / 4 <= circ_x <= win_w * 3 / 4 + 15 and win_h / 3 <= circ_y - 50 <= win_h / 3 + 160:
        #     circ_y = win_h / 3 + 210
        #     neg_y = -neg_y
        if blue_c.colliderect(right):
            if circ_y >= win_h / 3 + 160 and not circ_y <= win_h / 3 + 130:
                circ_y = win_h / 3 + 210
                neg_y = -neg_y
            if circ_y <= win_h / 3 and not circ_y >= win_h / 3 + 10:
                circ_y = win_h / 3 - 50
                neg_y = -neg_y

        # Side Wall
        if 630 <= circ_x + 50 <= 640 and 0 <= circ_y <= 100:
            circ_x = win_w - 60
            neg_x = -neg_x
        if 630 <= circ_x + 50 <= 640 and win_h * 2 / 3 <= circ_y <= win_h * 2 / 3 + 100:
            circ_x = win_w - 60
            neg_x = -neg_x
        if circ_x - 50 <= 0:
            circ_x = 50
            neg_x = -neg_x
        if circ_y + 50 >= win_h:
            screen_01 = True
            circ_y = 51
            screen_02 = False
        if circ_x + 50 >= win_w:
            circ_x = 51
            screen_03 = True
            screen_02 = False
        if circ_y - 50 <= 0:
            circ_y = 50
            neg_y = -neg_y

    if screen_03:
        win.fill((255, 255, 255))
        pygame.draw.rect(win, (0, 0, 0), (int(win_w / 4), int(win_h / 3), 25, 160))
        pygame.draw.rect(win, (0, 0, 0), (0, 0, 10, 100))
        pygame.draw.rect(win, (0, 0, 0), (0, int(win_h * 2 / 3), 10, 100))
        pygame.draw.rect(win, (0, 0, 0), (300, win_h - 10, 150, 10))
        red = pygame.draw.circle(win, (255, 0, 0), (500, 240), 50)

        # Block
        if win_w / 4 <= circ_x + 50 <= win_w / 4 + 25 and win_h / 3 <= circ_y <= win_h / 3 + 160:
            circ_x = win_w / 4 - 50
            neg_x = -neg_x
        if win_w / 4 <= circ_x - 50 <= win_w / 4 + 25 and win_h / 3 <= circ_y <= win_h / 3 + 160:
            circ_x = win_w / 4 + 75
            neg_x = -neg_x
        if win_w / 4 <= circ_x <= win_w / 4 + 25 and win_h / 3 <= circ_y + 50 <= win_h / 3 + 160:
            circ_y = win_h / 3 - 50
            neg_y = -neg_y
        if win_w / 4 <= circ_x <= win_w / 4 + 25 and win_h / 3 <= circ_y - 50 <= win_h / 3 + 160:
            circ_y = win_h / 3 + 210
            neg_y = -neg_y

        # Circle
        if blue_c.collidepoint(500, 240):
            screen_01 = True
            vibrate = True
            direction = True
            circ_x = win_w / 2
            circ_y = win_h / 2
            screen_03 = False

        # Side Walls
        if 0 <= circ_x - 50 <= 10 and 0 <= circ_y <= 100:
            circ_x = 60
            neg_x = -neg_x
        if 0 <= circ_x - 50 <= 10 and win_h * 2 / 3 <= circ_y <= win_h * 2 / 3 + 100:
            circ_x = 60
            neg_x = -neg_x
        if win_h - 10 <= circ_y + 50 <= win_h and 250 <= circ_x <= 400:
            circ_y = win_h - 60
        if circ_x - 50 <= 0:
            circ_x = win_w - 51
            screen_02 = True
            screen_03 = False
        if circ_y + 50 >= win_h:
            circ_y = 51
            screen_04 = True
            screen_03 = False
        if circ_x + 50 >= win_w:
            circ_x = win_w - 50
            neg_x = -neg_x
        if circ_y - 50 <= 0:
            circ_y = 50
            neg_y = -neg_y

    if screen_04:
        win.fill((255, 255, 255))
        pygame.draw.rect(win, (0, 0, 0), (0, int(win_h / 3), 10, 160))
        pygame.draw.rect(win, (0, 0, 0), (250, 0, 150, 10))
        pygame.draw.rect(win, (0, 0, 0), (250, int(win_h / 2), 150, 25))

        # Side Walls
        if circ_x - 50 <= 0:
            screen_01 = True
            circ_x = win_w - 51
            screen_04 = False
        if circ_y + 50 >= win_h:
            circ_y = win_h - 50
            neg_y = -neg_y
        if circ_x + 50 >= win_w:
            circ_x = win_w - 50
            neg_x = -neg_x
        if circ_y - 50 <= 0:
            circ_y = win_h - 51
            screen_03 = True
            screen_04 = False
        if 0 <= circ_y - 50 <= 10 and 250 <= circ_x <= 400:
            circ_y = 60
            neg_y = -neg_y
        if 10 >= circ_x - 50 >= 0 and win_h / 3 <= circ_y <= win_h / 3 + 160:
            circ_x = 60
            neg_x = -neg_x
        if 250 <= circ_x + 50 <= 400 and win_h / 2 <= circ_y <= win_h / 2 + 25:
            circ_x = 200
            neg_x = -neg_x
        if 250 <= circ_x - 50 <= 400 and win_h / 2 <= circ_y <= win_h / 2 + 25:
            circ_x = 450
            neg_x = -neg_x
        if 250 <= circ_x <= 400 and win_h / 2 <= circ_y + 50 <= win_h / 2 + 25:
            circ_y = win_h / 2 - 50
            neg_y = -neg_y
        if 250 <= circ_x <= 400 and win_h / 2 <= circ_y - 50 <= win_h / 2 + 25:
            circ_y = win_h / 2 + 75
            neg_y = -neg_y

    # Quiting
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            run = False
    if event.type == pygame.QUIT:
        run = False
pygame.quit()
