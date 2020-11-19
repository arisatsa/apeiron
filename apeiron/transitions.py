# coding: utf-8

from enum import auto, Enum

class Transition(Enum):
    SET  = auto()
    POP  = auto()
    PUSH = auto()
    NONE = auto()