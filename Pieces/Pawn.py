from typing import List, Tuple
import pygame

from Pieces.ChessPiece import ChessPiece
from Utils.Colours import Colour


class Pawn(ChessPiece):
    def __init__(self, screen: pygame.Surface, colour: Colour, pos: Tuple[int, int], board: List[List[ChessPiece]]):
        super().__init__(screen, colour, pos, board)
        self.moved = False

    @property
    def validMoves(self) -> List[Tuple[int, int]]:
        movement = 1 if self.colour == Colour.white else -1  # Up or Down movement based on black or white
        moves = []

        try:
            if otherPiece := self._board[self.y + movement][self.x - 1]:
                if otherPiece.colour != self._colour:
                    moves.append((self.x-1, self.y + movement))
        except IndexError:
            pass

        try:
            if otherPiece := self._board[self.y + movement][self.x + 1]:
                if otherPiece.colour != self._colour:
                    moves.append((self.x + 1, self.y + movement))
        except IndexError:
            pass

        try:
            if self._board[self.y+movement][self.x] is None:
                moves.append((self.x, self.y+movement))
                if self._board[self.y+movement+movement][self.x] is None and self.moved is False:
                    moves.append((self.x, self.y + movement + movement))
        except IndexError:
            pass

        return moves

    def draw(self, xy: Tuple[int, int], size: int, selected: bool = False):
        if selected:
            pygame.draw.circle(self._screen, Colour.green.value, xy, size)
        else:
            pygame.draw.circle(self._screen, self.colour.value, xy, size)
        pygame.draw.circle(self._screen, Colour.gray.value, xy, size, 4)  # Outline
