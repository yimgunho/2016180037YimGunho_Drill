import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *
import main_state
import game_world


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


big_ball_count = 5


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = (random.randint(50, 1280 - 50), random.randint(50, 824 - 50))
        self.check = False

    def get_bb(self):
        return self.x - 10.5, self.y - 10.5, self.x + 10.5, self.y + 10.5

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        global big_ball_count
        balls = main_state.get_ball()
        zombie = main_state.get_zombie()
        if big_ball_count <= 0 and collide(zombie, self):
            balls.remove(self)
            game_world.remove_object(self)
            zombie.hp += 50

    def reset(self):
        if self.check:
            self.x, self.y = (random.randint(50, 1280 - 50), random.randint(50, 824 - 50))


class BigBall(Ball):
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = (random.randint(50, 1280 - 50), random.randint(50, 824 - 50))

    def get_bb(self):
        return self.x - 20.5, self.y - 20.5, self.x + 20.5, self.y + 20.5

    def update(self):
        global big_ball_count
        balls = main_state.get_ball()
        zombie = main_state.get_zombie()
        if collide(zombie, self):
            balls.remove(self)
            game_world.remove_object(self)
            big_ball_count -= 1
            zombie.hp += 100

