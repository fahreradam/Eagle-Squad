from player import Player
import random

class Enemy(Player):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.position = [x, y]


    def movement(self, dt):
        if self.position[0] >= 0:
            self.random_x = random.randint(-100, 100)
            self.random_y = random.randint(-100, 100)
            # self.position[0] += 100 * dt
            self.position[0] += self.random_x * dt
            self.position[1] += self.random_y * dt

