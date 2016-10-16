
import random
from pico2d import *
import Stage
import character
import Backstage

running = None


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def main():

    open_canvas(800, 800)

    backstage = Backstage.BackStage()
    Character = character.Character()
    stage = Stage.Stage()

    global running
    running = True

    while running:
        handle_events()

        Character.update()
        clear_canvas()
        backstage.draw()
        stage.draw()
        Character.draw()
        update_canvas()

        delay(0.04)

    close_canvas()


if __name__ == '__main__':
    main()