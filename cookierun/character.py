from pico2d import *


class Character:
    image_init = None

    def __init__(self):
        self.x = 100
        self.y = 240
        self.frame = 1
        self.state = "run"
        self.jump_state = "up"
        self.slide_count = 0

        if self.image_init == None:
            self.run = load_image('image\\cookie_run.png')
            self.jump = load_image('image\\cookie_run_jump.png')
            self.slide = load_image('image\\cookie_run_slide.png')

    def update(self):
        self.frame += 1
        if self.frame == 6:
            self.frame = 1

        if self.state == "jump" and self.jump_state == "up":
            if self.y >= 400:
                self.jump_state = "down"
            self.y += 15

        if self.state == "jump" and self.jump_state == "down":
            if self.y >= 250:
                self.y -= 15

        if self.state == "jump" and self.y == 240:
            self.state = "run"
            self.jump_state = "up"

        if self.state == "slide":
            self.y = 220


    def draw(self):
        if self.state == "run":
            self.run.clip_draw(self.frame * 75, 0, 75, 87, self.x, self.y)
        elif self.state == "jump":
            self.jump.draw(self.x, self.y)
        elif self.state == "slide":
            self.slide.draw(self.x, self.y)





