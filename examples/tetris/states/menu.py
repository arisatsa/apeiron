# coding: utf-8

from apeiron import (
    draw, trans,
    pygame, State)

from tetris import states

class Menu(State):
    def handle_keydown_event(self, event):
        if event.key in [pygame.K_p, pygame.K_ESCAPE]:
            return trans.POP()

    def handle_mousebuttondown_event(self, event):
        return trans.SET(states.GameState)

    def draw(self):
        draw.clear(self.ctx, (255, 255 * (not getattr(self.ctx, 'paused', 0)), 255))