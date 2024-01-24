from tic_tac_toe.enums import PieceType


class Player:
    def __init__(self, name: str, piece: PieceType):
        self.name = name
        self.piece = piece
