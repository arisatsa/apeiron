# coding: utf-8

import pygame

from .utils import call_func
from .state import State, StateManager
from .transitions import Transition as Trans

class Context:
    def __init__(self, **config):
        self.config = config
        self.configure_ctx()

        self.state_manager = StateManager()

    def configure_ctx(self):
        pygame.init()

        pygame.event.set_grab(self.config['grab_mouse'])
        pygame.mouse.set_visible(self.config['show_mouse'])
        pygame.display.set_caption(self.config['title'])

        self.clock  = pygame.time.Clock()
        self.flags  = pygame.RESIZABLE  *  self.config['resizable'] | \
                      pygame.FULLSCREEN * self.config['fullscreen']
        self.screen = pygame.display.set_mode(self.config['size'], self.flags)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                while self.state_manager.state:
                    self.state_manager.pop()

                exit(pygame.quit() or 0)

            if self.state_manager.state:
                event_name = pygame.event.event_name(event.type).lower()
                transition = call_func(self.state_manager.state, f'handle_{event_name}_event', event)

                if transition:
                    state = transition[1](self) if transition[1] else None
                    {
                        Trans.SET : lambda s: self.state_manager.set_state(s),
                        Trans.POP : lambda s: self.state_manager.pop(),
                        Trans.PUSH: lambda s: self.state_manager.push(s)
                    }.get(transition[0], lambda s: None)(state)

    def run(self, initial_state):
        # TODO: ????

        self.state_manager.push(initial_state(self))

        while True and self.state_manager.state:
            self.handle_events()
            call_func(self.state_manager.state, 'update')
            call_func(self.state_manager.state, 'draw')
            self.clock.tick(60)
            pygame.display.flip()

        exit(pygame.quit() or 0)

class ContextBuilder:
    def __init__(self, title, width, height):
        self.config = {
            'title'     : title,
            'size'      : (width, height),
            'vsync'     : False,
            'resizable' : False,
            'fullscreen': False,
            'show_mouse': True,
            'grab_mouse': False
        }

    def __str__(self):
        return str(self.config)

    def __getattr__(self, name): # poggers?
        if name in self.config.keys():
            return lambda d: self.config.update({name: d}) or self

    def build(self):
        return Context(**self.config)