from player import Player
import random
import math

class Enemy(Player):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.position = [x, y]
        self.timer = 100
        self.speed = 100
        self.random_direction1 = [-80, 80, 0]
        self.random_direction2 = [-80, 80, 0]
        self.dir1 = 0
        self.dir2 = 0
        self.orientation = 180

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

    def distanceto(self, playerx, playery):
        self.distance = math.sqrt((self.position[0] - playerx) ** 2 + (self.position[1] - playery) ** 2)

    def movetowards(self, direction, delta_time):
        dist = self.speed * direction * delta_time
        radians = math.radians(self.orientation)
        opposite = -dist * math.sin(radians)
        adjacent = dist * math.cos(radians)
        self.position[0] += adjacent
        self.position[1] += opposite

    def point_towards(self, target_pt):
        adjacent = target_pt[0] - self.position[0]
        opposite = -(target_pt[1] - self.position[1])
        self.orientation = math.degrees(math.atan2(opposite, adjacent))

