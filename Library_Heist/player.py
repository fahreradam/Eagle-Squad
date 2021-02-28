import pygame


class Player:
    def __init__(self, x, y, surf):
        self.position = [x, y]
        self.img = pygame.image.load("images\\DO NOT USE. ONLY  FOR TESTING.png")
        self.img_scale = pygame.transform.scale(self.img, (50, 50))
        self.win = surf
        self.size = [self.img_scale.get_width(), self.img_scale.get_height()]
        self.img_scale.set_colorkey((255, 255, 255))
        self.speed = 100

    def draw(self):
        self.win.blit(self.img_scale, self.position)

    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.position[0] -= self.speed * dt
        if keys[pygame.K_d]:
            self.position[0] += self.speed * dt
        if keys[pygame.K_w]:
            self.position[1] -= self.speed * dt
        if keys[pygame.K_s]:
            self.position[1] += self.speed * dt
