from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 824
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
running = True
frame = 0
dir_x = 0
dir_y = 0
stop = 1


def handle_events():
    # fill here
    global running, dir_x, dir_y, stop
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
                stop = 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
                stop = -1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
    pass


def character_move():
    global dir_x, dir_y, x, y
    if x > 21 and dir_x < 0:
        x += dir_x * 10
    elif x < 1259 and dir_x > 0:
        x += dir_x * 10
    if y < 778 and dir_y > 0:
        y += dir_y * 10
    elif y > 41 and dir_y < 0:
        y += dir_y * 10
    pass


def character_animation():
    global dir_x, dir_y, x, y
    if dir_x < 0:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    elif dir_x > 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif dir_x == 0:
        if stop < 0:
            if dir_y != 0:
                character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
            else:
                character.clip_draw(100, 100 * 2, 100, 100, x, y)
        elif stop > 0:
            if dir_y != 0:
                character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
            else:
                character.clip_draw(100, 100 * 3, 100, 100, x, y)


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character_animation()
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    character_move()

    delay(0.01)

close_canvas()
