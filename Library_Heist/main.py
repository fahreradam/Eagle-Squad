import pygame
import player
import objectives
import menu

pygame.init()

win_w = 800
win_h = 600
win = pygame.display.set_mode((win_w, win_h))
map = pygame.image.load("images\\Map.png")
map_scale = pygame.transform.scale(map, (win_w, win_h))

# Class importing
player = player.Player(11, 413, win)
power = objectives.Power(0, 0, win)
books = objectives.Bookshelves(500, 0, win)
bathroom = objectives.Bathroom(0, 400, win)
menu_vars = menu.Variables()

screen = "main_menu"
clock = pygame.time.Clock()

done = False
while not done:
    delta_time = clock.tick() / 1000
    event = pygame.event.poll()
    keys = pygame.key.get_pressed()
    (mx, my) = pygame.mouse.get_pos()
    (mouseLeft, mouseMiddle, mouseRight) = pygame.mouse.get_pressed()

    # Determining which "Screen" (Main Menu, Credits, Goals, Game)

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
        win.blit(map_scale, (0, 0))
        player.draw()
        bathroom.timer(delta_time, player.position)
        bathroom.draw()
        bathroom.number2(player.position)
        books.draw()
        books.read(player.position)
        books.collect(player.position, event)
        power.draw()
        player.move(delta_time)
        power.collide(player.position)

    # Exiting
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            done = True
    if event.type == pygame.QUIT:
        done = True
    pygame.display.flip()
