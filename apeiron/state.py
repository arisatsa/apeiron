# coding: utf-8

from .utils import call_func

class State:
    def __init__(self, ctx):
        self.ctx = ctx

    def __str__(self):
        return self.__class__.__name__

class StateManager:
    def __init__(self):
        self.states = []

    @property
    def state(self):
        try:
            return self.states[-1]
        except IndexError:
            return None

    def push(self, state):
        if not isinstance(state, State):
            raise Exception('can we have sex now?')

        call_func(self.state, 'on_pause')
        self.states.append(state)
        call_func(self.state, 'on_start')

    def pop(self):
        if self.state:
            call_func(self.state, 'on_stop')
            self.states.pop()
            call_func(self.state, 'on_resume')

    def set_state(self, state):
        if self.state:
            call_func(self.state, 'on_stop')
            self.states.pop()

        self.states.append(state)
        call_func(self.state, 'on_start')