from pico2d import *
import random
import json

hurdle_data_file = open('MapData\\stage1-1', 'r')
hurdle_data = json.load(hurdle_data_file)
hurdle_data_file.close()

hurdle_data_file2 = open('MapData\\stage1-2', 'r')
hurdle_data2 = json.load(hurdle_data_file2)
hurdle_data_file2.close()


################################################################






class Hurdle1:
    global hurdle_data
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


        if Hurdle1.image == None:
            self.hurdle11 = load_image('image\\hurdle1-1.png')

    def create(self):
        hurdle_state = {
            "hurdle1" : self.image
        }

        hurdle = []
        for name in hurdle_data:
            hur = Hurdle1()
            hur.name = name
            hur.x = hurdle_data[name]['x']
            hur.y = hurdle_data[name]['y']
            hur.state = hurdle_state[hurdle_data[name]['state']]
            hurdle.append(hur)

        return hurdle


    def update(self, frame_time):
        if Hurdle1.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 10
        else:
            self.distance = Hurdle1.RUN_SPEED_PPS * frame_time

        self.x -= self.distance

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 15, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def draw(self):
        self.hurdle11.draw(self.x, self.y)

class Hurdle12:
    global hurdle_data2
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


        if Hurdle12.image == None:
            self.hurdle12 = load_image('image\\hurdle1-2.png')

    def create(self):
        hurdle_state = {
            "hurdle1" : self.image
        }

        hurdle = []
        for name in hurdle_data2:
            hur = Hurdle12()
            hur.name = name
            hur.x = hurdle_data2[name]['x']
            hur.y = hurdle_data2[name]['y']
            hur.state = hurdle_state[hurdle_data2[name]['state']]
            hurdle.append(hur)

        return hurdle


    def update(self, frame_time):
        if Hurdle12.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 10
        else:
            self.distance = Hurdle1.RUN_SPEED_PPS * frame_time

        self.x -= self.distance

    def get_bb(self):
        return self.x - 50, self.y - 210, self.x + 50, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        self.hurdle12.draw(self.x, self.y)


class Hurdle2:
    global hurdle_data
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


        if Hurdle1.image == None:
            self.hurdle11 = load_image('image\\hurdle1-1.png')

    def create(self):
        hurdle_state = {
            "hurdle1" : self.image
        }

        hurdle = []
        for name in hurdle_data:
            hur = Hurdle1()
            hur.name = name
            hur.x = hurdle_data[name]['x']
            hur.y = hurdle_data[name]['y']
            hur.state = hurdle_state[hurdle_data[name]['state']]
            hurdle.append(hur)

        return hurdle


    def update(self, frame_time):
        if Hurdle1.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 10
        else:
            self.distance = Hurdle1.RUN_SPEED_PPS * frame_time

        self.x -= self.distance

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 15, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def draw(self):
        self.hurdle11.draw(self.x, self.y)