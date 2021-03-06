import pygame


class Player:
    def __init__(self, x, y):
        self.position = [x, y]
        self.img = pygame.image.load("images\\tile_0431.png")
        self.img_scale = pygame.transform.scale(self.img, (30, 30))
        self.img_scale.set_colorkey((0, 0, 0))
        self.speed = 100
        self.bathroom = pygame.Rect(479, 480, 33, 24)
        self.health = 3

    def draw(self, surf):
        surf.blit(self.img_scale, self.position)

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

    def main_collision(self):
        """Collision of the walls"""
        # Collision with y for the walls
        if self.position[1] + 30 >= 433 and self.position[0] <= 122:
            self.position[1] = 433 - 30
        if self.position[1] + 30 >= 457 and self.position[0] <= 156:
            self.position[1] = 457 - 30
        if self.position[1] + 30 >= 481 and self.position[0] <= 189:
            self.position[1] = 481 - 30
        if self.position[1] + 30 >= 504 and self.position[0] <= 253:
            self.position[1] = 504 - 30
        if self.position[1] + 30 >= 528 and self.position[0] <= 284:
            self.position[1] = 528 - 30
        if self.position[1] + 30 >= 552:
            self.position[1] = 552 - 30
        if self.position[1] + 30 >= 433 and 484 <= self.position[0] + 30 <= 511:
            if 505 >= self.position[1] + 30 >= 479:
                pass
            else:
                self.position[1] = 433 - 30
        if self.position[1] + 30 >= 409 and 516 <= self.position[0] + 30 <= 539:
            self.position[1] = 409 - 30
        if self.position[1] + 30 >= 385 and 545 <= self.position[0] + 30 <= 572:
            self.position[1] = 385 - 30
        if self.position[1] + 30 >= 361 and 578 <= self.position[0] + 30 <= 764:
            self.position[1] = 361 - 30
        if self.position[1] + 30 >= 337 and 770 <= self.position[0] + 30:
            self.position[1] = 337 - 30
        if self.position[1] <= 0:
            self.position[1] = 0

        # Collision with x
        if self.position[0] <= 0:
            self.position[0] = 0
        if self.position[0] <= 130 and self.position[1] >= 434 - 30:
            self.position[0] = 130
        if self.position[0] <= 162 and self.position[1] >= 458 - 30:
            self.position[0] = 162
        if self.position[0] <= 195 and self.position[1] >= 482 - 30:
            self.position[0] = 195
        if self.position[0] <= 261 and self.position[1] >= 505 - 30:
            self.position[0] = 261
        if self.position[0] <= 292 and self.position[1] >= 529 - 30:
            self.position[0] = 292
        if self.position[0] + 30 >= 472 and 554 >= self.position[1] + 30 >= 504:
            self.position[0] = 472 - 30
        if self.position[0] + 30 >= 472 and 481 >= self.position[1] + 30 >= 434:
            self.position[0] = 472 - 30
        if self.position[0] + 30 >= 503 and 433 >= self.position[1] + 30 >= 410:
            self.position[0] = 503 - 30
        if self.position[0] + 30 >= 535 and 410 >= self.position[1] + 30 >= 388:
            self.position[0] = 535 - 30
        if self.position[0] + 30 >= 568 and 388 >= self.position[1] + 30 >= 364:
            self.position[0] = 568 - 30
        if self.position[0] + 30 >= 759 and 364 >= self.position[1] + 30 >= 338:
            self.position[0] = 759 - 30
        if self.position[0] + 30 >= 793:
            self.position[0] = 793 - 30

        """Collision of Objects"""
        # Desk and Printer
        if pygame.Rect(0, 374, 156, 10).collidepoint(self.position[0] + 15, self.position[1] + 20):
            self.position[1] = 384 - 20
        if pygame.Rect(0, 361, 156, 10).collidepoint(self.position[0] + 15, self.position[1] + 30):
            self.position[1] = 361 - 30
        if pygame.Rect(140, 172, 20, 213).collidepoint(self.position[0] + 7, self.position[1] + 30):
            self.position[0] = 160 - 7
        if pygame.Rect(140, 172, 20, 213).collidepoint(self.position[0] + 23, self.position[1] + 30):
            self.position[0] = 140 - 23
        if pygame.Rect(65, 171, 92, 22).collidepoint(self.position[0] + 7, self.position[1] + 30):
            if self.position[1] + 30 <= 175:
                self.position[1] = 170 - 30
            if self.position[1] + 30 >= 180:
                self.position[1] = 193 - 30
            if 67 <= self.position[0] <= 65:
                self.position[0] = 65
        if pygame.Rect(0, 171, 32, 22).collidepoint(self.position[0] + 7, self.position[1] + 30):
            if self.position[1] + 30 <= 175:
                self.position[1] = 170 - 30
            if self.position[1] + 30 >= 180:
                self.position[1] = 193 - 30
            if 32 <= self.position[0] <= 30:
                self.position[0] = 32

        if pygame.Rect(609, 170, 124, 32).collidepoint(self.position[0] + 15, self.position[1] + 30):
            if self.position[1] + 30 <= 171:
                self.position[1] = 170 - 30
            if self.position[1] + 30 >= 200:
                self.position[1] = 202 - 30
        if pygame.Rect(609, 170, 124, 32).collidepoint(self.position[0] + 23, self.position[1] + 30):
            if self.position[0] + 23 <= 610:
                self.position[0] = 609 - 23
        if pygame.Rect(609, 170, 124, 32).collidepoint(self.position[0] + 7, self.position[1] + 30):
            if self.position[0] + 7 >= 730:
                self.position[0] = 733 - 7

        if pygame.Rect(258, 218, 187, 32).collidepoint(self.position[0] + 15, self.position[1] + 30):
            if self.position[1] + 30 <= 220:
                self.position[1] = 218 - 30
            if self.position[1] + 30 >= 249:
                self.position[1] = 250 - 30
        if pygame.Rect(258, 218, 187, 32).collidepoint(self.position[0] + 23, self.position[1] + 30):
            if self.position[0] + 23 <= 260:
                self.position[0] = 258 - 23
        if pygame.Rect(258, 218, 187, 32).collidepoint(self.position[0] + 7, self.position[1] + 30):
            if self.position[0] + 7 >= 443:
                self.position[0] = 445 - 7

        if pygame.Rect(482, 218, 254, 32).collidepoint(self.position[0] + 15, self.position[1] + 30):
            if self.position[1] + 30 <= 220:
                self.position[1] = 218 - 30
            if self.position[1] + 30 >= 249:
                self.position[1] = 250 - 30
        if pygame.Rect(482, 218, 254, 32).collidepoint(self.position[0] + 23, self.position[1] + 30):
            if self.position[0] + 23 <= 484:
                self.position[0] = 482 - 23
        if pygame.Rect(482, 218, 254, 32).collidepoint(self.position[0] + 7, self.position[1] + 30):
            if self.position[0] + 7 >= 734:
                self.position[0] = 736 - 7

        if pygame.Rect(258, 266, 188, 32).collidepoint(self.position[0] + 15, self.position[1] + 30):
            if self.position[1] + 30 <= 268:
                self.position[1] = 266 - 30
            if self.position[1] + 30 >= 296:
                self.position[1] = 298 - 30
        if pygame.Rect(258, 266, 188, 32).collidepoint(self.position[0] + 23, self.position[1] + 30):
            if self.position[0] + 23 <= 259:
                self.position[0] = 258 - 23
        if pygame.Rect(258, 266, 188, 32).collidepoint(self.position[0] + 7, self.position[1] + 30):
            if self.position[0] + 7 >= 444:
                self.position[0] = 446 - 7

        if pygame.Rect(482, 266, 254, 32).collidepoint(self.position[0] + 15, self.position[1] + 30):
            if self.position[1] + 30 <= 268:
                self.position[1] = 266 - 30
            if self.position[1] + 30 >= 296:
                self.position[1] = 298 - 30
        if pygame.Rect(482, 266, 254, 32).collidepoint(self.position[0] + 23, self.position[1] + 30):
            if self.position[0] + 23 <= 484:
                self.position[0] = 482 - 23
        if pygame.Rect(482, 266, 254, 32).collidepoint(self.position[0] + 7, self.position[1] + 30):
            if self.position[0] + 7 >= 734:
                self.position[0] = 736 - 7

        if pygame.Rect(258, 314, 188, 32).collidepoint(self.position[0] + 15, self.position[1] + 30):
            if self.position[1] + 30 <= 316:
                self.position[1] = 314 - 30
            if self.position[1] + 30 >= 344:
                self.position[1] = 346 - 30
        if pygame.Rect(258, 314, 188, 32).collidepoint(self.position[0] + 23, self.position[1] + 30):
            if self.position[0] + 23 <= 260:
                self.position[0] = 258 - 23
        if pygame.Rect(258, 314, 188, 32).collidepoint(self.position[0] + 7, self.position[1] + 30):
            if self.position[0] + 7 >= 444:
                self.position[0] = 446 - 7

        if pygame.Rect(482, 314, 254, 32).collidepoint(self.position[0] + 15, self.position[1] + 30):
            if self.position[1] + 30 <= 316:
                self.position[1] = 314 - 30
            if self.position[1] + 30 >= 344:
                self.position[1] = 346 - 30
        if pygame.Rect(482, 314, 254, 32).collidepoint(self.position[0] + 23, self.position[1] + 30):
            if self.position[0] + 23 <= 484:
                self.position[0] = 482 - 23
        if pygame.Rect(482, 314, 254, 32).collidepoint(self.position[0] + 7, self.position[1] + 30):
            if self.position[0] + 7 >= 734:
                self.position[0] = 736 - 7

    def bath_collisions(self):
        if self.position[0] <= 0:
            if 95 <= self.position[1] + 7 and self.position[1] + 50 <= 145:
                pass
            else:
                self.position[0] = 0
        if self.position[0] + 50 >= 432:
            self.position[0] = 432 - 50
        if self.position[1] <= 0:
            self.position[1] = 0
        if self.position[1] + 50 >= 241:
            self.position[1] = 241 - 50
