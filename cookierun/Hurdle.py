from pico2d import *
import random
import json

hurdle_data_file = open('MapData\\stage1-1', 'r')
hurdle_data = json.load(hurdle_data_file)
hurdle_data_file.close()

hurdle_len_file = open('MapData\\stage1', 'r')
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

    def update(self, frame_time, Count_copy):
        global Hurdle_Start1, random_draw1

        if Count_copy >= 1:
            self.Hurdle_Start1 = True

        if self.Hurdle_Start1 == True and self.state != "Collid":
            self.hurdle_move(frame_time)
            self.sum = 0

        elif self.Hurdle_Start1 == True and self.state == "Collid":
            if self.sum < 30:

                self.sum += 10
                for i in range(2):
                    if self.x > 150:
                        self.x += 20
                    else:
                        self.x -= 20

        self.x -= self.distance

        def create(self, num):
            hurdle = []
            for i in range(2):
                self.name = "현오"
                self.x = hurdle_data[i]['x']
                self.y = hurdle_data[i]['y']
                hurdle.append(self)

            return hurdle

    #def draw(self):
   #     self.hurdle1.draw(self.x, self.y)

    def draw(self):
        if self.Hurdle_Start1 == True:
            self.image.draw(self.x, self.y)
