import pygame


class Power:
    def __init__(self, x, y, surf):
        self.win = surf
        self.position = [x, y]
        self.img = pygame.draw.rect(self.win, (255, 0, 0), (50, 50, 100, 100))

    def draw(self):
        pygame.draw.rect(self.win, (255, 0, 0), (50, 50, 100, 100))

    def collide(self, player):
        if self.img.collidepoint(player):
            print('yes')
