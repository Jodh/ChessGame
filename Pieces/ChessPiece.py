from abc import ABC, abstractmethod
from typing import List, Tuple

import pygame

from Utils.Colours import Colour


class ChessPiece(ABC, object):

    def __init__(self, screen: pygame.Surface, colour: Colour, position: Tuple[int, int], board: List[List["ChessPiece"]]):
        self._screen = screen
        self._colour = colour
        self._board = board
        self.position = position

    @property
    def x(self) -> int:
        return self.position[0]

    @property
    def y(self) -> int:
        return self.position[1]

    @property
    def colour(self) -> Colour:
        return self._colour

    @property
    @abstractmethod
    def validMoves(self) -> List[Tuple[int, int]]:
        raise NotImplementedError()

    @abstractmethod
    def draw(self, xy: Tuple[int, int], size: int, selected: bool = False):
        raise NotImplementedError()
