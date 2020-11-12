# coding: utf-8

def call_func(obj, name, *a, **k):
    if obj:
        return getattr(obj, name, lambda *a, **k: None)(*a, **k)