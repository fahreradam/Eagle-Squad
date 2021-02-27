import pygame
import random


class Power:
    def __init__(self, x, y, surf):
        self.win = surf
        self.position = [x, y]
        self.img = pygame.draw.rect(self.win, (255, 0, 0), (self.position[0], self.position[1], 100, 100))
        self.font = pygame.font.SysFont("Arial", 32)

    def draw(self):
        pygame.draw.rect(self.win, (255, 0, 0), (self.position[0], self.position[1], 100, 100))

    def collide(self, player):
        if self.img.collidepoint((player[0] + 25, player[1] + 25)):
            self.win.blit(self.font.render("Press E to turn on power", True, (255, 255, 255)), player)
            if pygame.key.get_pressed()[pygame.K_e]:
                self.win.blit(self.font.render("You have turned on the power", True, (255, 255, 255)), player)


class Bookshelves:
    """Still needs randomized position"""

    def __init__(self, x, y, surf):
        self.win = surf
        self.position = [x, y]
        self.img = pygame.draw.rect(self.win, (255, 0, 0), (self.position[0], self.position[1], 100, 100))
        self.font = pygame.font.SysFont("Arial", 32)
        self.text = self.font.render("Press E to pick up book", True, (255, 255, 255))
        self.book = 0
        self.book_left = 2

    def draw(self):
        pygame.draw.rect(self.win, (255, 0, 0), (self.position[0], self.position[1], 100, 100))

    def collide(self, player):
        if self.img.collidepoint((player[0] + 25, player[1] + 25)):
            self.win.blit(self.font.render("Press E to grab book", True, (255, 255, 255)), player)
            if pygame.key.get_pressed()[pygame.K_e]:
                self.win.blit(
                    self.font.render(("You have" + str(self.book) + "books. You have" + str(self.book_left) + "books "
                                                                                                              "left"),
                                     True, (255, 255, 255)), player)


class Bathroom:
    def __init__(self, x, y, surf):
        self.win = surf
        self.time = random.randint(20, 120)
        self.clock = 0
        # self.img = pygame.image.load("images\\")
        self.position = [x, y]
        self.font = pygame.font.SysFont("Arial", 32)

    # def draw(self):
    #   self.win.blit(self.img, self.position)

    def timer(self, dt, player):
        self.clock += dt
        if self.time <= int(self.clock) <= self.time + 5:
            self.win.blit(self.font.render("I need to use the bathroom", True, (255, 255, 255)), (250, 0))
