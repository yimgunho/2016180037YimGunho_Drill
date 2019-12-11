import pickle

import game_framework
from pico2d import *
import main_state
import world_build_state
import world_build_state as start_state

name = "RankingState"
font = None
records = []


def get_ranking_data():
    global records

    with open('record_data.json', 'r') as f:
        data_str = f.read()
        data = json.loads(data_str)
        records = data
        print(records)


def enter():
    global font
    font = load_font('ENCR10B.TTF')
    get_ranking_data()
    hide_cursor()
    hide_lattice()
    print('ranking')


def exit():
    pass


def update(): pass


def draw():
    clear_canvas()
    font.draw(200, 900, '[Total Ranking]', (0, 0, 0))
    i = 1
    for record in records:
        font.draw(200, 900 - i * 50, '#%d %2.2f' % (i, record), (0, 0, 0))
        i += 1
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)


def pause(): pass


def resume(): pass
