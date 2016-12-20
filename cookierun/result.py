from pico2d import *
from character import *
import game_framework
import title_state
import main_state
import main_state2

score = None
title = None
result = None
font = None
image = None

def enter():
    global title, result, font, score
    title = load_image('image\\title.png')
    result = load_image('image\\result.png')
    font = load_font('image\\ENCR10B.TTF', 100)
    score = Character()




def exit():
    global image
    del(image)


def handle_events():
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

            elif event.type == SDL_MOUSEMOTION:
                x, y = event.x, 599 - event.y



def draw():
    global font, score
    clear_canvas()
    result.draw(400, 300)
    font.draw(290, 380, '%3.2d' % score.score)
    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass