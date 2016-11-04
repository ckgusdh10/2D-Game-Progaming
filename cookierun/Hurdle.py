from pico2d import *
import random
import json

class Hurdle1:
    image_init = None

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    count = 0
    posx = 600
    def __init__(self):
         pass

    def update(self, frame_time):
        if Hurdle1.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 10
        else:
            self.distance = Hurdle1.RUN_SPEED_PPS * frame_time

        self.x -= self.distance



    def draw(self):
        self.hurdle1.draw(self.x, self.y)


