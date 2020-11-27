# coding: utf-8

from .states import MenuState
from apeiron import ContextBuilder

if __name__ == "__main__":
    ContextBuilder('tetris', 600, 520) \
        .grab_mouse(False) \
        .resizable(False) \
        .fps(75) \
        .build() \
        .run(MenuState)