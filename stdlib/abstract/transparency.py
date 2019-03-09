"""
transparency.py
=========================================================
The transparency.py module for python stdlib
"""
from abc import ABC


class Transparency(ABC):
    OPAQUE = 1
    BITMASK = 2
    TRANSLUCENT = 3

    def get_transparency(self) -> int:
        ...
