import pygame
import player
import menu
pygame.init()

win_w = 800
win_h = 600
win = pygame.display.set_mode((win_w, win_h))
player = player.Player(400, 300, win)
clock = pygame.time.Clock()

screen = "credits"

menu_vars = menu.Variables()


done = False
while not done:
    delta_time = clock.tick() / 1000
    event = pygame.event.poll()
    keys = pygame.key.get_pressed()
    (mx, my) = pygame.mouse.get_pos()
    (mouseLeft,mouseMiddle,mouseRight) = pygame.mouse.get_pressed()

    #Determining which "Screen" (Main Menu, Credits, Goals, Game)

    if screen == "main_menu":
        if mouseLeft == True:
            if mx > 350 and mx < 470 and my > 150 and my < 200:
                screen = "game"

            if mx > 345 and mx < 475 and my > 200 and my < 250:
                screen = "goals"

            if mx > 325 and mx < 490 and my > 250 and my < 300:
                screen = "credits"

            if mx > 370 and mx < 455 and my > 350 and my < 400:
                done = True

        menu.draw_menu(win, menu_vars)

    if screen == "goals":
        menu.draw_goals_screen(win, menu_vars)
        if mouseLeft == True:
            if mx > 10 and mx < 780 and my > 530 and my < 580:
                screen = "main_menu"


    if screen == "credits":
        menu.draw_credits_screen(win, menu_vars)
        if mouseLeft == True:
            if mx > 10 and mx < 780 and my > 530 and my < 580:
                screen = "main_menu"


    if screen == "game":
        player.draw()
        player.move(delta_time)

    # Exiting
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            done = True
    if event.type == pygame.QUIT:
        done = True

    pygame.display.update()
