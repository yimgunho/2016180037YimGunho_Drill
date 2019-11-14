import game_framework
from pico2d import *
import main_state

name = "PauseState"
image = None


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del image


def update(): pass


def draw():
    global image
    clear_canvas()
    image.draw(400, 300, 200, 200)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.pop_state()


def pause(): pass


def resume(): pass
