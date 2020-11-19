# coding: utf-8

import pygame

from apeiron import graphics
from apeiron.state import State
from apeiron.context import ContextBuilder
from apeiron.transitions import Transition as Trans

class PausedState(State):
    def on_start(self):
        print('started', self)

    def on_stop(self):
        print('stopped', self)

    def handle_keydown_event(self, event):
        return {
            pygame.K_ESCAPE: (Trans.POP, None),
        }.get(event.key, (Trans.NONE, None))

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
            pygame.K_ESCAPE: ( Trans.POP, None),
            pygame.K_s     : ( Trans.SET, PausedState),
            pygame.K_p     : (Trans.PUSH, PausedState)
        }.get(event.key, (Trans.NONE, None))

    def update(self):
        pass

    def draw(self):
        graphics.clear(self.ctx, (0, 0, 0))

if __name__ == '__main__':
    ContextBuilder('test', 400, 400) \
        .vsync(True) \
        .grab_mouse(False) \
        .show_mouse(False) \
        .resizable(True) \
        .build() \
        .run(MainState)