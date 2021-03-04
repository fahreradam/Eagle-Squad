import pygame
import player
import objectives
import menu
import pickle
import os
from os import path
import time
import enemy
# import tiled

pygame.init()

win_w = 800
win_h = 600
win = pygame.display.set_mode((win_w, win_h))
main_room = pygame.image.load("images\\Tester.png")
maps = [pygame.transform.scale(main_room, (win_w, win_h)), pygame.image.load("images\\Bathroom.png")]
current_map = maps[0]
screen = "main_menu"
level = "main_room"


# Class importing
player = player.Player(21, 385)
enemy = enemy.Enemy(400, 200)
power = objectives.Power(0, 0, win)
books = objectives.Bookshelves(500, 0, win)
bathroom = objectives.Bathroom(0, 400, win)
menu_vars = menu.Variables()


clock = pygame.time.Clock()
menuClock = 0
game_clock = 0
blank_list = []  # This is just for writing the Save File, other than that no use.
game_playing = False

pygame.mixer.init()  # This is used for the Music. Credit to ID Software
pygame.mixer.music.load("e1m1.wav")
#pygame.mixer.music.play(-1)

if path.exists("times.dat"):
    print("Loading Saved Data...")
    prev_times = pickle.load(open("times.dat", "rb"))

else:
    print("Creating Save File")
    pickle.dump(blank_list, open("times.dat", "wb"))
    prev_times = []

save_time = False


def menu_clock():
    global menuClock
    menuClock = pygame.time.get_ticks() / 1000  # This determins how long the user is in the Menus, used for the in-game timer.


done = False
while not done:
    delta_time = clock.tick() / 1000
    event = pygame.event.poll()
    keys = pygame.key.get_pressed()
    (mx, my) = pygame.mouse.get_pos()
    (mouseLeft, mouseMiddle, mouseRight) = pygame.mouse.get_pressed()

    # Determining which "Screen" (Main Menu, Credits, Goals, Game)
    if pygame.mouse.get_pressed()[0]:
        print((mx, my))
    if screen == "main_menu":
        menu_clock()
        if save_time == True:
            prev_times.append(round(game_clock, 2))
            game_clock = 0
            save_time = False

        if mouseLeft == True:
            if mx > 350 and mx < 470 and my > 150 and my < 200:
                screen = "game"
                game_playing = True

            if mx > 345 and mx < 475 and my > 200 and my < 250:
                screen = "goals"

            if mx > 325 and mx < 490 and my > 250 and my < 300:
                screen = "credits"

            if mx > 250 and mx < 575 and my > 300 and my < 350:
                screen = "prev_times"

            if mx > 370 and mx < 455 and my > 400 and my < 450:
                done = True

        menu.draw_menu(win, menu_vars)

    if screen == "goals":
        menu_clock()
        menu.draw_goals_screen(win, menu_vars)
        if mouseLeft == True:
            if mx > 10 and mx < 780 and my > 530 and my < 580:
                if game_playing == False:
                    screen = "main_menu"

                else:
                    screen = "game"
                    win.fill((0, 0, 0))

    if screen == "prev_times":
        menu_clock()
        menu.draw_prev_times_screen(win, menu_vars, prev_times)
        if mouseLeft == True:
            if mx > 10 and mx < 780 and my > 530 and my < 580:
                screen = "main_menu"

    if screen == "credits":
        menu_clock()
        menu.draw_credits_screen(win, menu_vars)
        if mouseLeft == True:
            if mx > 10 and mx < 780 and my > 530 and my < 580:
                screen = "main_menu"

    if screen == "game":
        win.fill((0, 0, 0))
        win.blit(current_map, (0, 0))

        player.draw(win)
        bathroom.timer(delta_time)
        player.move(delta_time)
        enemy.draw(win)
        enemy.movement(delta_time)

        game_clock = pygame.time.get_ticks() / 1000 - menuClock  # This is used for how long the game is played.

        if level == "main_room":
            books.read(player.position)
            books.collect(player.position, event)
            power.printing(player.position)
            player.main_collision()
            enemy.main_collision()
            if player.bathroom.collidepoint(player.position[0] + 15, player.position[1] + 15):
                level = "bathroom"
                player.position = [0, 98]
            if keys[pygame.K_b]:
                level = "bathroom"
                player.position = [0, 90]


        if level == "bathroom":
            current_map = maps[1]
            player.img_scale = pygame.transform.scale(player.img, (50, 50))
            bathroom.number2(player.position)
            power.collide(player.position)

        if keys[pygame.K_BACKSPACE]:  # This emulates the game "ending". All three pieces of code need to be put in
            screen = "main_menu"  # wherever the actual "game ending" code is.
            save_time = True
            game_playing = False

        if keys[pygame.K_o]:  # This is Purely for Testing.
            screen = "goals"
            game_playing = True

    # Exiting
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            done = True
    if event.type == pygame.QUIT:
        done = True
    pygame.display.flip()

pickle.dump(prev_times, open("times.dat", "wb"))
