# coding: utf-8

import pygame

from apeiron import (
    draw, trans,
    State, ContextBuilder)

class PausedState(State):
    def handle_keydown_event(self, event):
        return {
            pygame.K_ESCAPE: trans.POP(),
        }.get(event.key, trans.NONE())

    def draw(self):
        draw.clear(self.ctx, (255, 255, 255))
        pygame.draw.rect(self.ctx.screen, (0, 0, 0), self.ctx.rect)

class MainState(State):
    def on_start(self):
        self.ctx.rect = pygame.Rect(0, 200, 10, 10)

    def handle_keydown_event(self, event):
        return {
            pygame.K_ESCAPE: trans.POP(),
            pygame.K_s     : trans.SET(PausedState),
            pygame.K_p     : trans.PUSH(PausedState)
        }.get(event.key, trans.NONE())

    def update(self):
        self.ctx.rect.move_ip(1, 0)

    def draw(self):
        draw.clear(self.ctx, (0, 0, 0))
        pygame.draw.rect(self.ctx.screen, (255, 255, 255), self.ctx.rect)

if __name__ == '__main__':
    ContextBuilder('test', 400, 400) \
        .icon(pygame.Surface((1, 1))) \
        .grab_mouse(False) \
        .resizable(True) \
        .fps(75) \
        .build() \
        .run(MainState)