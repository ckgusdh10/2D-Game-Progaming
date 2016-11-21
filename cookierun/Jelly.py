from pico2d import *
import random
import json

jelly_data_file = open('MapData\\jelly', 'r')
jelly_data = json.load(jelly_data_file)
jelly_data_file.close()

################################################

class Jelly:
    global jelly_data
    image = None
    state = "None"
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.speed = 10
        self.distance = 0

        if Jelly.image == None:
            self.jelly = load_image('image\\jelly.png')

    def create(self):
        hurdle_state = {
            "jelly": self.image
        }
        jelly = []
        for name in jelly_data:
            jel = Jelly()
            jel.name = name
            jel.x = jelly_data[name]['x']
            jel.y = jelly_data[name]['y']
            jel.state = hurdle_state[jelly_data[name]['state']]
            jelly.append(jel)

        return jelly

    def update(self, frame_time):
        if Jelly.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 10
        else:
            self.distance = Jelly.RUN_SPEED_PPS * frame_time

        self.x -= self.distance

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 15, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.jelly.draw(self.x, self.y)