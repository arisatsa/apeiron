# coding: utf-8

class State:
    def __init__(self, ctx):
        self.ctx = ctx

    def __str__(self):
        return self.__class__.__name__

    def __getattr__(self, name):
        if name in ['on_start', 'on_stop', 'on_pause', 'on_resume']:
            return lambda *a, **k: None

        raise AttributeError(name)

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
            raise Exception('`state` must be an instance of `State`')

        if self.state:
            self.state.on_pause()

        self.states.append(state)
        self.state.on_start()

    def pop(self):
        if not self.state:
            raise Exception('state stack is empty')

        self.state.on_stop()
        self.states.pop()

        if self.state:
            self.state.on_resume()

    def set_state(self, state):
        if not isinstance(state, State):
            raise Exception('`state` must be an instance of `State`')

        if self.state:
            self.state.on_stop()
            self.states.pop()

        self.states.append(state)
        self.state.on_start()