import pygame
import random
import time


class Power:
    def __init__(self, x, y, surf):
        self.win = surf
        self.position = [x, y]
        self.img = pygame.draw.rect(self.win, (255, 0, 0), (self.position[0], self.position[1], 100, 100))
        self.font = pygame.font.SysFont("Arial", 32)
        self.power_on = False
        self.pc = [pygame.Rect(102, 192, 56, 24), pygame.Rect(102, 239, 56, 24), pygame.Rect(102, 286, 56, 24), pygame.Rect(102, 333, 56, 24)]
        self.printer = pygame.Rect(34, 318, 57, 44)
        self.print = False
        self.paper = False

    def collide(self, player):
        if self.img.collidepoint((player[0] + 25, player[1] + 25)) and not self.power_on:
            if pygame.key.get_pressed()[pygame.K_e]:
                self.win.blit(self.font.render("You have turned on the power", True, (255, 255, 255)), player)
                pygame.display.flip()
                time.sleep(1)
                self.power_on = True
            else:
                self.win.blit(self.font.render("Press E to turn on power", True, (255, 255, 255)), player)

    def printing(self, player):
        if self.pc[0].collidepoint(player[0] + 25, player[1] + 25) and self.power_on and not self.print:
            if pygame.key.get_pressed()[pygame.K_e] and not self.print:
                self.win.blit(self.font.render("I wonder where it printed", True, (255, 255, 255)), player)
                pygame.display.flip()
                time.sleep(1)
                self.print = True
            else:
                self.win.blit(self.font.render("Press E to print", True, (255, 255, 255)), player)
        if self.printer.collidepoint((player[0] + 25, player[1] + 25)) and self.print and not self.paper:
            if pygame.key.get_pressed()[pygame.K_e] and not self.paper:
                self.win.blit(self.font.render("You've collected the paper", True, (255, 255, 255)), player)
                pygame.display.flip()
                time.sleep(1)
                self.paper = True
            else:
                self.win.blit(self.font.render("Press E to collect paper", True, (255, 255, 255)), player)


class Bookshelves:
    """Still needs randomized position"""

    def __init__(self, x, y, surf):
        self.win = surf
        self.position = [x, y]
        self.bookshelves = [pygame.Rect(609, 170, 124, 32), pygame.Rect(258, 218, 187, 32), pygame.Rect(482, 220, 254, 32), pygame.Rect(257, 266, 188, 32), pygame.Rect(483, 287, 254, 32), pygame.Rect(257, 314, 188, 32), pygame.Rect(481, 314, 254, 32)]
        self.tables = [pygame.Rect(159, 36, 95, 54), pygame.Rect(321, 36, 95, 54), pygame.Rect(483, 36, 95, 54), pygame.Rect(645, 36, 95, 54), pygame.Rect(321, 127, 95, 54), pygame.Rect(483, 127, 95, 54)]
        self.font = pygame.font.SysFont("Arial", 32)
        self.text = self.font.render("Press E to pick up book", True, (255, 255, 255))
        self.book = 0
        self.book_left = 2
        self.read_book = False
        self.collected = False

    def collect(self, player, event):
        if self.bookshelves[2].collidepoint((player[0] + 25, player[1] + 25)) and not self.collected:
            if pygame.key.get_pressed()[pygame.K_e]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.book += 1
                self.win.blit(
                    self.font.render(
                        ("You have " + str(self.book) + " books. You have " + str(self.book_left) + " books "
                                                                                                    "left"),
                        True, (255, 255, 255)), player)
            elif self.book == self.book_left:
                self.collected = True

            else:
                self.win.blit(self.font.render("Press E to grab book", True, (255, 255, 255)), player)

    def read(self, player):
        if self.book >= 1 and not self.read_book:
            if self.tables[5].collidepoint(player[0] + 25, player[1] + 25):
                if pygame.key.get_pressed()[pygame.K_e]:
                    self.win.blit(self.font.render("You have read the book", True, (255, 255, 255)), player)
                    pygame.display.flip()
                    time.sleep(1)
                    self.read_book = True
                else:
                    self.win.blit(self.font.render("Press E to read book", True, (255, 255, 255)), player)


class Bathroom:
    def __init__(self, x, y, surf):
        self.win = surf
        self.time = random.randint(20, 80)
        self.clock = 0
        self.position = [x, y]
        self.toilet = [pygame.Rect(57, 164, 32, 68), pygame.Rect(153,  164, 32, 68), pygame.Rect(249,  164, 32, 68), pygame.Rect(345, 164, 32, 68)]
        self.font = pygame.font.SysFont("Arial", 32)
        self.flush = True
        self.need = False

    def timer(self, dt):
        self.clock += dt
        if self.time <= int(self.clock) <= self.time + 5:
            self.win.blit(self.font.render("I need to use the bathroom", True, (255, 255, 255)), (250, 0))
            self.flush = False

    def number2(self, player):
        if self.toilet[0].collidepoint((player[0] + 25, player[1] + 25)) and not self.flush:
            if pygame.key.get_pressed()[pygame.K_e] and not self.flush:
                self.win.blit(self.font.render("I feel better now", True, (255, 255, 255)), player)
                pygame.display.flip()
                time.sleep(1)
                self.flush = True
            else:
                self.win.blit(self.font.render("Press E to go number 2", True, (255, 255, 255)), player)
