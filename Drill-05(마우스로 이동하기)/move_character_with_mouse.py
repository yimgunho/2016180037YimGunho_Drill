from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 824
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')
hide_cursor()

play = True
frame = 0
now_x, now_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
default_x, default_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
cursor_x, cursor_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
dir_x = 0
mouse_button = 0
stop = 1
i = 0
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2


def handle_events():
    global play, default_x, default_y, now_x, now_y, dir_x, mouse_button
    global cursor_x, cursor_y, i, x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            play = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                play = False
        elif event.type == SDL_MOUSEMOTION:
            cursor_x, cursor_y = event.x, KPU_HEIGHT - 1 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            mouse_button += 1
            i = 0
            default_x, default_y = x, y
            now_x, now_y = event.x, KPU_HEIGHT - 1 - event.y
            if default_x < event.x:
                dir_x = 1;
            elif default_x > event.x:
                dir_x = -1;


while play:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if i == 0 and dir_x >= 0:
        character.clip_draw(100, 100 * 3, 100, 100, default_x, default_y)
    elif i == 0 and dir_x < 0:
        character.clip_draw(100, 100 * 2, 100, 100, default_x, default_y)

    if i < 101 and mouse_button > 0:
        i += 1
        t = i / 100
        x = (1 - t) * default_x + t * now_x
        y = (1 - t) * default_y + t * now_y
        if default_x < now_x:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif default_x >= now_x:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        if i >= 100:
            i = 0
            mouse_button = 0
            default_x = now_x
            default_y = now_y

    cursor.draw(cursor_x + 25, cursor_y - 26)

    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    delay(0.01)

close_canvas()
