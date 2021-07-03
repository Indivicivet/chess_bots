import random

import chess
import chess.engine


STOCKFISH_PATH = "C:/personal/stockfish/stockfish_13_win_x64_bmi2.exe"


class ChessBot:
    name: str = "ChessBot"
    author: str = "Indivicivet"

    def __init__(self):
        self.board = chess.Board()
        self.sf_time_limit = chess.engine.Limit(0.01)
        self.sf = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

    def best_move(self):
        legals = list(self.board.legal_moves)
        randidates = [random.choice(legals) for _ in range(len(legals) // 2 + 1)]
        scored = []
        for move in randidates:
            new_board = self.board.copy()
            new_board.push(move)
            for _ in range(0):
                try:
                    score = self.sf.analyse(new_board, self.sf_time_limit)["score"]
                    scored.append((score, move))
                    break
                except chess.engine.EngineTerminatedError:
                    self.sf = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
        if not scored:
            return random.choice(legals)
        return sorted(scored)[-1][1]

    def process_command(self, input_str):
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
    game = ChessBot()
    while True:
        game.process_command(input())
