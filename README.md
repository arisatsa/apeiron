# apeiron
raw pygame is not nice. there will be minimal activity as i'll work on this whenever i feel like. relevant docs about implementation: [amethyst/concepts/state](https://book.amethyst.rs/stable/concepts/state.html#state), [tetra/ContextBuilder](https://docs.rs/tetra/0.5.6/tetra/struct.ContextBuilder.html)

```python
# coding: utf-8

from apeiron import (
    draw, trans, pygame,
    State, ContextBuilder)

class PausedState(State):
    def handle_keydown_event(self, event):
        if event.key in [pygame.K_p, pygame.K_ESCAPE]:
            return trans.POP()

        return trans.NONE()

    def draw(self):
        draw.clear(self.ctx, (255, 255, 255))
        draw.rect(self.ctx, (0, 0, 0), self.ctx.rect)

class MainState(State):
    def on_start(self):
        self.ctx.rect = pygame.Rect(0, 0, 10, 10)

    def handle_keydown_event(self, event):
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
```
