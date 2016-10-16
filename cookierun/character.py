from pico2d import *


class Character:
    image_init = None

    def __init__(self):
        self.x = 40
        self.y = 240
        self.frame = 1
        self.character1 = load_image('image\\cookie_run.png')

    def update(self):
        self.frame += 1
        if self.frame == 6:
            self.frame = 1

    def draw(self):
        self.character1.clip_draw(self.frame * 75, 0, 75, 87, self.x, self.y)