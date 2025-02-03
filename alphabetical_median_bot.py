"""
AlphaMove
https://xkcd.com/3045/

however this currently doesn't do that since str vers of moves are in CUI notation :(
"""

import sys
from dataclasses import dataclass

import base_uci_bot


@dataclass
class AlphaMoveBot(base_uci_bot.BaseUCIBot):
    name: str = "AlphaMove"
    author: str = "indivicivet"

    def select_move(self):
        moves = sorted(self.board.legal_moves, key=lambda m: str(m))
        sys.stderr.write(", ".join(map(str, moves)))
        sys.stderr.flush()
        return moves[len(moves) // 2]


if __name__ == "__main__":
    game = AlphaMoveBot()
    while True:
        game.process_command(input())
