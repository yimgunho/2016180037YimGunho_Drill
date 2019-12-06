import random
import math
import game_framework
from pico2d import *
import main_state
import game_world


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = (random.randint(50, 1800), random.randint(50, 1040))

    def get_bb(self):
        return self.x - 10.5, self.y - 10.5, self.x + 10.5, self.y + 10.5

    def draw(self):
        self.image.draw(self.x - self.wl, self.y - self.wb, 40, 40)

    def update(self):
        self.wl = self.bg.window_left
        self.wb = self.bg.window_bottom

    def set_background(self, bg):
        self.bg = bg
