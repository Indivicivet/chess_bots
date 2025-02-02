import random
import sys

import chess


class RandomMoveBot:
    name: str = "RandomMoveBot"
    author: str = "Indivicivet"

    def __init__(self):
        self.board = chess.Board()

    def best_move(self):
        return random.choice(list(self.board.legal_moves))

    def process_command(self, input_str):
        sys.stderr.write(f"got command `{input_str}`\n")
        sys.stderr.flush()
        cmd, *params = input_str.split(" ")
        if cmd == "uci":
            print(f"id name {self.name}")
            print(f"id author {self.author}")
            print("uciok")
        elif cmd == "isready":
            print("readyok")
        elif cmd == "ucinewgame":
            self.board = chess.Board()
        elif cmd == "position":
            assert params
            if params[0] == "startpos":
                self.board = chess.Board()
            elif params[0] == "fen":
                self.board = chess.Board(" ".join(params[1:]))
            else:
                raise Exception("bad param after `position` cmd")
            if len(params) > 1:
                assert len(params) >= 3
                for move in params[2:]:
                    self.board.push_uci(move)
        elif cmd == "go":
            move = self.best_move()
            print(f"bestmove {move}")
            self.board.push(move)
        elif cmd in ["exit", "quit"]:
            exit()


if __name__ == "__main__":
    game = RandomMoveBot()
    while True:
        game.process_command(input())
