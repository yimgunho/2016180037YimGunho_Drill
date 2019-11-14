import game_framework
from pico2d import *

import game_world

BIRD_SIZE = 70  # 2m 10cm

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
FLY_SPEED_KMPH = 40.0  # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class FlyState:

    @staticmethod
    def enter(bird, event):
        pass


    @staticmethod
    def exit(bird, event):
        pass

    @staticmethod
    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        bird.x += bird.velocity * game_framework.frame_time
        bird.x = clamp(35, bird.x, 1600 - 35)
        if bird.x >= 1600 - 35:
            bird.dir -= 1
            bird.velocity = -FLY_SPEED_PPS

        elif bird.x <= 35:
            bird.dir += 1
            bird.velocity = FLY_SPEED_PPS

    @staticmethod
    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw((int(bird.frame) % 5) * 182, (2 - (int(bird.frame) // 5)) * 168, 182, 168,
                                 bird.x, bird.y, BIRD_SIZE, BIRD_SIZE)

        else:
            bird.image.clip_composite_draw((int(bird.frame) % 5) * 182, (2 - (int(bird.frame) // 5)) * 168, 182, 168,
                                           0, 'h', bird.x, bird.y, BIRD_SIZE, BIRD_SIZE)

class Bird:
    def __init__(self):
        self.x, self.y = 1600 // 2, 400
        self.image = load_image('bird_animation.png')
        self.dir = 1
        self.velocity = FLY_SPEED_PPS
        self.frame = 0
        self.cur_state = FlyState

    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)




