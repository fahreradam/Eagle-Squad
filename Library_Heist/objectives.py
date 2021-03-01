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
        self.pc = pygame.draw.rect(self.win, (100, 100, 100), (400, 300, 100, 100))
        self.printer = pygame.draw.rect(self.win, (100, 255, 100), (100, 500, 100, 100))
        self.print = False
        self.paper = False

    def draw(self):
        pygame.draw.rect(self.win, (255, 0, 0), (self.position[0], self.position[1], 100, 100))
        pygame.draw.rect(self.win, (100, 100, 100), (400, 300, 100, 100))
        pygame.draw.rect(self.win, (100, 255, 100), (100, 500, 100, 100))

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
        if self.pc.collidepoint((player[0] + 25, player[1] + 25)) and self.power_on and not self.print:
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
        self.bookshelf = pygame.draw.rect(self.win, (255, 0, 0), (self.position[0], self.position[1], 100, 100))
        self.table = pygame.draw.rect(self.win, (255, 0, 0), (self.position[0], self.position[1] + 200, 100, 100))
        self.font = pygame.font.SysFont("Arial", 32)
        self.text = self.font.render("Press E to pick up book", True, (255, 255, 255))
        self.book = 0
        self.book_left = 2
        self.read_book = False
        self.collected = False

    def draw(self):
        pygame.draw.rect(self.win, (255, 0, 0), (self.position[0], self.position[1], 100, 100))
        pygame.draw.rect(self.win, (255, 255, 0), (self.position[0], self.position[1] + 200, 100, 100))

    def collect(self, player, event):
        if self.bookshelf.collidepoint((player[0] + 25, player[1] + 25)) and not self.collected:
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
            if self.table.collidepoint((player[0] + 25, player[1] + 25)):
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
        self.toilet = pygame.draw.rect(self.win, (0, 0, 255), (self.position[0], self.position[1], 50, 50))
        self.font = pygame.font.SysFont("Arial", 32)
        self.flush = True
        self.need = False

    def draw(self):
        pygame.draw.rect(self.win, (0, 0, 255), (self.position[0], self.position[1], 50, 50))

    def timer(self, dt):
        self.clock += dt
        if self.time <= int(self.clock) <= self.time + 5:
            self.win.blit(self.font.render("I need to use the bathroom", True, (255, 255, 255)), (250, 0))
            self.flush = False

    def number2(self, player):
        if self.toilet.collidepoint((player[0] + 25, player[1] + 25)) and not self.flush:
            if pygame.key.get_pressed()[pygame.K_e] and not self.flush:
                self.win.blit(self.font.render("I feel better now", True, (255, 255, 255)), player)
                pygame.display.flip()
                time.sleep(1)
                self.flush = True
            else:
                self.win.blit(self.font.render("Press E to go number 2", True, (255, 255, 255)), player)
