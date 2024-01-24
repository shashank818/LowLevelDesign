from collections import deque
from typing import List

from tic_tac_toe.board import Board
from tic_tac_toe.player import Player


class Game:
    def __init__(self, players: List[Player], size: int):
        self.players = deque(players)
        self.size = size
        self.board = Board(self.size)
        self.current_player = self.players[0]

    def switch_player(self):
        self.players.rotate(-1)
        self.current_player = self.players[0]

    def start_game(self):
        no_winner = True

        while no_winner:
            self.board.print_board()
            free_spaces = self.board.get_free_cells()
            if not free_spaces:
                no_winner = False
                continue

            print("Player: " + self.current_player.name + "Enter row colum: ")
            row, col = map(int, input().split(","))

