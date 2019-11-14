import random
from pico2d import *
import game_world
import game_framework


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600 - 1), 60, 0
        self.dir = None
        self.move_speed = None
        self.check = False

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

    def stop(self):
        self.fall_speed = 0

    def brick_move(self, dir, move_speed):
        if self.y >= 230:
            self.fall_speed = 0
        if self.fall_speed == 0:
            self.y = 240

        if dir >= 1:
            self.x += move_speed * game_framework.frame_time
        else:
            self.x -= move_speed * game_framework.frame_time

        self.x = clamp(20, self.x, 1600 - 20)

    def reset(self):
        if self.check:
            self.x, self.y = random.randint(0, 1600 - 1), 500
            self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED, BigBall.MAX_FALL_SPEED)


class BigBall(Ball):
    MIN_FALL_SPEED = 50  # 50 pps = 1.5 meter per sec
    MAX_FALL_SPEED = 200  # 200 pps = 6 meter per sec
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1600 - 1), 500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED, BigBall.MAX_FALL_SPEED)
        self.check = True

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


