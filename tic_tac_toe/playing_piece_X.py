from tic_tac_toe.playing_piece import PlayingPiece
from tic_tac_toe.enums import PieceType


class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)
