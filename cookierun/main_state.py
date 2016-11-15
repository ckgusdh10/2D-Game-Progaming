import random
from pico2d import *
from Stage import *
from character import *
from Backstage import *
from Hurdle import *
from Jelly import *

import game_framework
import title_state

running = None
current_time = 0.0
stage = None
character = None
backstage = None
hurdle = None
hurdle2 = None
jelly = None

name = "MainState"

def collid(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global stage, character, backstage, running, hurdle, hurdle2, jelly
    backstage = BackStage()
    stage = Stage()
    character = Character()
    hurdle = Hurdle1().create()
    hurdle2 = Hurdle12().create()
    jelly = Jelly().create()
    running = True

def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def exit():
    global stage, character, backstage, running, hurdle, hurdle2, jelly
    del(stage)
    del(character)
    del(backstage)
    for hur in hurdle:
        hurdle.remove(hur)
        del(hur)
    del(hurdle)

    for hur in hurdle2:
        hurdle2.remove(hur)
        del(hur)
    del(hurdle2)

    for jel in jelly:
        jelly.remove(jel)
        del(jel)
    del(jelly)

def pause():
    pass


def resume():
    pass
def update():
    global running, backstage, character, stage, hurdle

    handle_events()
    frame_time = get_frame_time()
    backstage.update(frame_time)
    character.update()
    stage.update(frame_time)


    for hur in hurdle:
        hur.update(frame_time)
        if collid(character, hur):
            character.state = "collid"

    for hur in hurdle2:
        hur.update(frame_time)
        if collid(character, hur):
            character.state = "collid"

    for jel in jelly:
        jel.update(frame_time)
        if collid(character, jel):
            jelly.remove(jel)

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
         #   running = False
        else:

            if event.type == SDL_KEYDOWN and event.key == SDLK_z:
                if character.state != "collid":
                    character.state = "jump"
            elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
                if character.state != "collid":
                    character.state = "slide"
            elif event.type == SDL_KEYUP and event.key == SDLK_x:
                character.state = "run"
                character.y = 240
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)

def draw():
    global backstage, stage, character, running
    clear_canvas()
    backstage.draw()
    stage.draw()
    character.draw()
    character.draw_bb()

    for hur in hurdle:
        hur.draw()
        hur.draw_bb()

    for hur in hurdle2:
        hur.draw()
        hur.draw_bb()

    for jel in jelly:
        jel.draw()
        jel.draw_bb()

    # for Hurdle1 in Hur:
    #   Hurdle1.draw()
    delay(0.04)
    update_canvas()

#    close_canvas()
