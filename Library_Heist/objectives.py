import pygame


class Power:
    def __init__(self, x, y, player, surf):
        self.position = [x, y]
        self.player = player
        self.img = pygame.draw.rect(surf, (255, 0, 0), (50, 50, 100, 100))

    def collide(self):
        if self.img.colliderect(self.player):
            print('yes')
