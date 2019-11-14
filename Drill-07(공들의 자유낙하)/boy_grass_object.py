from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 2

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Small_Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(50, 750), 599
        self.down = random.randint(2, 7)

    def update(self):
        if self.y >= 71:
            self.y -= self.down

    def draw(self):
        self.image.draw(self.x, self.y)


class Big_Ball:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(50, 750), 599
        self.down = random.randint(2, 7)

    def update(self):
        if self.y >= 81:
            self.y -= self.down

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
open_canvas()

small = random.randint(5, 15)
big = 20 - small

team = [Boy() for i in range(11)]
grass = Grass()

num1 = [Small_Ball() for i in range(small)]
num2 = [Big_Ball() for i in range(big)]
running = True

# game main loop code
while running:
    handle_events()

    for boy in team:
        boy.update()

    for n in num1:
        n.update()

    for n in num2:
        n.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for n in num1:
        n.draw()
    for n in num2:
        n.draw()
    update_canvas()

    delay(0.02)

# finalization code
close_canvas()
