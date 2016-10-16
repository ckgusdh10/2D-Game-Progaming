from pico2d import *

class BackStage:
    image_init = None

    def __init__(self):
        self.stage1 = load_image('image\\stage1-1.png')

    def draw(self):
        self.stage1.draw(400, 400)
