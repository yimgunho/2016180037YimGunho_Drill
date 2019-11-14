from pico2d import *


def handle_events():
    # fill here
    global running, dir, stop
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                stop = 1
            elif event.key == SDLK_LEFT:
                dir += 1
                stop = -1
    pass


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0
dir = 0
stop = 1

while running:
    clear_canvas()
    grass.draw(400, 30)
    if dir < 0:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, 90)
    elif dir > 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, 90)
    elif dir == 0:
        if stop < 0:
            character.clip_draw(100, 100 * 2, 100, 100, x, 90)
        elif stop > 0:
            character.clip_draw(100, 100 * 3, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    if x > 21 and dir < 0:
        x += dir * 5
    elif x < 779 and dir > 0:
        x += dir * 5

    delay(0.01)

close_canvas()
