from player import Player
import random

class Enemy(Player):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.position = [x, y]
        self.timer = 100
        self.random_direction1 = [-100, 100, 0]
        self.random_direction2 = [-100, 100, 0]
        self.dir1 = 0
        self.dir2 = 0

    def movement(self, dt):
        if self.timer > 0:
            self.position[0] -= self.dir1 * dt
            self.position[1] -= self.dir2 * dt
            self.timer -= 1
        elif self.timer == 0:
            self.dir1 = random.choice(self.random_direction1)
            self.dir2 = random.choice(self.random_direction2)
            self.timer = 200
            print(self.dir1)

