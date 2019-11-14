from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 824
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hide_cursor()

play = True
frame = 0
dir_x = 0
size = 10
i = 0
a = 0
pick_x = [random.randint(21, 1259) for i in range(size)]
pick_y = [random.randint(40, 780) for i in range(size)]
now_x, now_y = pick_x[0], pick_y[0]


def draw_curve_points():
    global pick_x, pick_y, dir_x, now_x, now_y, frame, i, a

    i += 2
    if i == 100:
        i = 0
        a += 1
        if a == 10:
            a = 0
    if a < 7:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * pick_x[a] + (3 * t ** 3 - 5 * t ** 2 + 2) * pick_x[a + 1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * pick_x[a + 2] + (t ** 3 - t ** 2) * pick_x[a + 3]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * pick_y[a] + (3 * t ** 3 - 5 * t ** 2 + 2) * pick_y[a + 1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * pick_y[a + 2] + (t ** 3 - t ** 2) * pick_y[a + 3]) / 2
    elif a == 7:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * pick_x[7] + (3 * t ** 3 - 5 * t ** 2 + 2) * pick_x[8] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * pick_x[9] + (t ** 3 - t ** 2) * pick_x[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * pick_y[7] + (3 * t ** 3 - 5 * t ** 2 + 2) * pick_y[8] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * pick_y[9] + (t ** 3 - t ** 2) * pick_y[0]) / 2
    elif a == 8:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * pick_x[8] + (3 * t ** 3 - 5 * t ** 2 + 2) * pick_x[9] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * pick_x[0] + (t ** 3 - t ** 2) * pick_x[1]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * pick_y[8] + (3 * t ** 3 - 5 * t ** 2 + 2) * pick_y[9] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * pick_y[0] + (t ** 3 - t ** 2) * pick_y[1]) / 2
    elif a == 9:
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * pick_x[9] + (3 * t ** 3 - 5 * t ** 2 + 2) * pick_x[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * pick_x[1] + (t ** 3 - t ** 2) * pick_x[2]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * pick_y[9] + (3 * t ** 3 - 5 * t ** 2 + 2) * pick_y[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * pick_y[1] + (t ** 3 - t ** 2) * pick_y[2]) / 2
    if now_x > x:
        dir_x = -1
    elif now_x < x:
        dir_x = 1

    now_x = x
    now_y = y


def handle_events():
    global play

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            play = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                play = False


while play:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    draw_curve_points()

    if dir_x >= 0:
        character.clip_draw(100 * frame, 100 * 1, 100, 100, now_x, now_y)
    elif dir_x < 0:
        character.clip_draw(100 * frame, 100 * 0, 100, 100, now_x, now_y)

    frame = (frame + 1) % 8

    update_canvas()

    handle_events()

    delay(0.01)

close_canvas()
