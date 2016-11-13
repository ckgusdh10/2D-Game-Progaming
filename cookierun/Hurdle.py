from pico2d import *
import random
import json

hurdle_data_file = open('MapData\\stage1-1.txt', 'r')
hurdle_data = json.load(hurdle_data_file)
hurdle_data_file.close()

hurdle_len_file = open('MapData\\stage1.txt', 'r')
len_data = json.load(hurdle_len_file)
hurdle_len_file.close()

################################################################






class Hurdle1:
    global hurdle_data
    image_init = None

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    STAND = 0


    def hurdle_move(self, frame_time):

        if Hurdle1.RUN_SPEED_PPS * frame_time > 13:
            self.distance = 5
        else:
            self.distance = Hurdle1.RUN_SPEED_PPS * frame_time
            # self.distance += (Hurdle.RUN_SPEED_PPS / 10) * (frame_time / 10000)
            self.x -= self.distance

    hurdle_state = {
        STAND: hurdle_move
    }

    def __init__(self, HurdleType, num):
        self.x = hurdle_data[HurdleType][num * 2]
        self.y = hurdle_data[HurdleType][num * 2 + 1]
        self.speed = 10
        self.distance = 0
        self.name = 'noname'
        self.image = None
        self.sum = 0
        self.width = 0
        self.height = 0
        self.arr = None
        self.rotate = False
        self.Hurdle_Start1 = False
        Hurdle1.nn += 1
        self.state = "None"
        print(self.x)
        if HurdleType == len_data['Stage1_Fork']['num']:
            self.arr = len_data['Stage1_Fork']
        elif HurdleType == len_data['Stage1_Fork2']['num']:
            self.arr = len_data['Stage1_Fork2']
        elif HurdleType == len_data['Stage1_thorn']['num']:
            self.arr = len_data['Stage1_thorn']
        elif HurdleType == len_data['big_jelly']['num']:
            self.arr = len_data['big_jelly']
        elif HurdleType == len_data['item_jelly']['num']:
            self.arr = len_data['item_jelly']

        self.image = load_image(self.arr['dir'])
        self.width = self.arr['width']
        self.height = self.arr['height']

    def update(self, frame_time):
        if Hurdle1.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 10
        else:
            self.distance = Hurdle1.RUN_SPEED_PPS * frame_time

        self.x -= self.distance



    #def draw(self):
   #     self.hurdle1.draw(self.x, self.y)

    def draw(self):
        if self.Hurdle_Start1 == True:
            self.image.draw(self.x, self.y)
