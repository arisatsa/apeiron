# coding: utf-8

from apeiron import graphics
from apeiron.state import State
from apeiron.context import ContextBuilder

class MainState(State):
    def on_start(self):
        print ('started pog', self)

    def on_stop(self):
        print ('stopped pog', self)

    def update(self):
        pass

    def draw(self, dt):
        graphics.clear(self.ctx, (255, 255, 255))

if __name__ == '__main__':
    ContextBuilder('test', 400, 400) \
        .vsync(True) \
        .grab_mouse(True) \
        .show_mouse(False) \
        .build() \
        .run(MainState)