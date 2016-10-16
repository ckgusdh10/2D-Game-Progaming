from pico2d import *

class Stage:
    image_init = None

    def __init__(self):
        self.stage1 = load_image('image\\stage1-0.png')

    def draw(self):
        self.stage1.draw(400, 400)

