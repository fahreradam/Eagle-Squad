import pygame


class Player:
    def __init__(self, x, y, surf):
        self.position = [x, y]
        self.img = pygame.image.load("images\\DO NOT USE. ONLY  FOR TESTING.png")
        self.win = surf

    def draw(self):
        self.win.blit(self.img, self.position)

    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.position[0] -= 50 * dt
        if keys[pygame.K_d]:
            self.position[0] += 50 * dt
        if keys[pygame.K_w]:
            self.position[1] -= 50 * dt
        if keys[pygame.K_s]:
            self.position[1] += 50 * dt
