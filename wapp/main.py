# coding: utf-8

import sys
import pygame

sys.path.append('..')

from random import randint
from apeiron import (
    draw, trans,
    State, ContextBuilder)

class PausedState(State):
    def handle_keydown_event(self, event):
        if event.key == pygame.K_p:
            self.ctx.pause.stop()
            self.ctx.resume.play()
            return trans.POP()

        return trans.NONE()

    def draw(self):
        draw.clear(self.ctx, (255, 255, 255))
        draw.rect(self.ctx, (0, 0, 0), self.ctx.rect)

class MainState(State):
    def on_start(self):
        self.ctx.rect = pygame.Rect(0, 0, 10, 10)
        self.ctx.pause = pygame.mixer.Sound('resources/pause.mp3')
        self.ctx.resume = pygame.mixer.Sound('resources/resume.mp3')

    def handle_keydown_event(self, event):
        if event.key == pygame.K_p:
            self.ctx.resume.stop()
            self.ctx.pause.play()

        return {
            pygame.K_p     : trans.PUSH(PausedState),
            pygame.K_s     : trans.SET(PausedState),
            pygame.K_ESCAPE: trans.POP()
        }.get(event.key, trans.NONE())

    def update(self):
        rect = self.ctx.rect
        size = self.ctx.config['size']

        if not (0 <= rect.x < size[0]):
            rect.x = max(0, size[0], key=lambda x: abs(rect.x - x))

        if not (0 <= rect.y < size[1]):
            rect.y = max(0, size[1], key=lambda y: abs(rect.y - y))

        rect.move_ip(randint(-10, 10), randint(-10, 10))

    def draw(self):
        draw.clear(self.ctx, (0, 0, 0))
        draw.rect(self.ctx, (255, 255, 255), self.ctx.rect)

if __name__ == '__main__':
    ContextBuilder('test', 200, 200) \
        .icon(pygame.Surface((1, 1))) \
        .grab_mouse(False) \
        .resizable(False) \
        .fps(75) \
        .build() \
        .run(MainState)