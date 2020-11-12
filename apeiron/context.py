# coding: utf-8

import pygame

from .utils import call_func
from .state import State, StateManager

pygame.init()

class Context:
    def __init__(self, **config):
        self.config = config
        self.configure_ctx()

        self.state_manager = StateManager()

    def configure_ctx(self):
        flags = pygame.RESIZABLE  * int(self.config['resizable']) | \
                pygame.FULLSCREEN * int(self.config['fullscreen'])
        self.screen = pygame.display.set_mode(self.config['size'], flags)

        pygame.event.set_grab(self.config['grab_mouse'])
        pygame.mouse.set_visible(self.config['show_mouse'])

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                while self.state_manager.state:
                    self.state_manager.pop()

                exit(pygame.quit() or 0)

    def run(self, initial_state):
        self.state_manager.push(initial_state(self))

        while True:
            call_func(self.state_manager.state, 'draw', 0)
            call_func(self.state_manager.state, 'update')
            self.handle_events()
            pygame.display.update()

class ContextBuilder:
    def __init__(self, title, width, height):
        self.config = {
            'title': title,
            'size' : (width, height),
            'vsync': False,
            'resizable': False,
            'fullscreen': False,
            'show_mouse': True,
            'grab_mouse': False}

    def __getattr__(self, name): # poggers?
        if name in self.config.keys():
            return lambda d: self.config.update({name: d}) or self

    def build(self):
        return Context(**self.config)