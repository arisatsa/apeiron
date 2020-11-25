# coding: utf-8

import sys
import pygame

sys.path.append('..')

from apeiron import (
    draw, trans,
    State, ContextBuilder)

class PausedState(State):
    def handle_keydown_event(self, event):
        self.ctx.pause.stop()
        if event.key == pygame.K_p:
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
        self.ctx.resume.stop()
        if event.key == pygame.K_p:
            self.ctx.pause.play()

        return {
            pygame.K_p     : trans.PUSH(PausedState),
            pygame.K_s     : trans.SET(PausedState),
            pygame.K_ESCAPE: trans.POP()
        }.get(event.key, trans.NONE())

    def update(self):
        if self.ctx.rect.x > self.ctx.config['size'][0]:
            self.ctx.rect.move_ip(-400, -400)

        self.ctx.rect.move_ip(1, 1)

    def draw(self):
        draw.clear(self.ctx, (0, 0, 0))
        draw.rect(self.ctx, (255, 255, 255), self.ctx.rect)

if __name__ == '__main__':
    ContextBuilder('test', 400, 400) \
        .icon(pygame.Surface((1, 1))) \
        .grab_mouse(False) \
        .resizable(True) \
        .fps(75) \
        .build() \
        .run(MainState)