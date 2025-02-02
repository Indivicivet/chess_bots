import random
from dataclasses import dataclass

import base_uci_bot


@dataclass
class RandomMoveBot(base_uci_bot.BaseUCIBot):
    name: str = "RandomMoveBot"
    author: str = "Indivicivet"

    def select_move(self):
        return random.choice(list(self.board.legal_moves))


if __name__ == "__main__":
    game = RandomMoveBot()
    while True:
        game.process_command(input())
