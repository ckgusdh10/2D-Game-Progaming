
import random
from pico2d import *
import Stage
import character
import Backstage
#import Hurdle


running = None
current_time = 0.0






def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def main():

    open_canvas(800, 800)

    backstage = Backstage.BackStage()
    stage = Stage.Stage()
    Character = character.Character()

  #  Hur = [Hurdle.Hurdle1() for i in range(10)]

    frame_time = get_frame_time()

    global running
    running = True

    def handle_events():
        global running

        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
                Character.state = "jump"
            elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
                Character.state = "slide"
            elif event.type == SDL_KEYUP and event.key == SDLK_x:
                Character.state = "run"
                Character.y = 240

    while running:
        handle_events()

        backstage.update(frame_time)
        Character.update()
        stage.update(frame_time)

       # for Hurdle1 in Hur:
        #    Hurdle1.update(frame_time)


        clear_canvas()

        backstage.draw()
        stage.draw()
        Character.draw()
        #for Hurdle1 in Hur:
         #   Hurdle1.draw()

        update_canvas()

        delay(0.04)





    close_canvas()


if __name__ == '__main__':
    main()