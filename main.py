# coding: utf-8

import pygame

from apeiron import trans
from apeiron import graphics
from apeiron.state import State
from apeiron.context import ContextBuilder

class PausedState(State):
    def on_start(self):
        print('started', self)

    def on_stop(self):
        print('stopped', self)

    def handle_keydown_event(self, event):
        return {
            pygame.K_ESCAPE: trans.POP(),
        }.get(event.key, trans.NONE())

    def update(self):
        pass

    def draw(self):
        graphics.clear(self.ctx, (255, 255, 255))

class MainState(State):
    def on_start(self):
        print('started', self)

    def on_stop(self):
        print('stopped', self)

    def handle_keydown_event(self, event):
        return {
            pygame.K_ESCAPE: trans.POP(),
            pygame.K_s     : trans.SET(PausedState),
            pygame.K_p     : trans.PUSH(PausedState)
        }.get(event.key, trans.NONE())

    def update(self):
        pass

    def draw(self):
        graphics.clear(self.ctx, (0, 0, 0))

if __name__ == '__main__':
    ContextBuilder('test', 400, 400) \
        .icon(pygame.Surface((1, 1))) \
        .grab_mouse(False) \
        .resizable(True) \
        .fps(60) \
        .build() \
        .run(MainState)