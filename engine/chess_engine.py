import chess
# To be replaced by BitBoard.board!
import sys
sys.path.append("/Users/littlecapa/GIT/python/ai_chess_engine_and_trainer/libs")
#/Users/littlecapa/GIT/python/ai_chess_engine_and_trainer/libs
from eval_lib import get_is_mate_value
import logging


class ChessEngine:

    def __init__(self):
        self.board = chess.Board()
        self.CHECKMATE_VALUE = get_is_mate_value()
        self.DRAW_VALUE = 0.0

    def __del__(self):
        pass

    def set_move_logger(self, move_log_file_path = ""):
        self.move_log_file_path = move_log_file_path
        pass

    def logger_on(self):
        self.logging = True

    def logger_off(self):
        self.logging = False

    #def get_logger_data(self):
    #    if self.logging:
    #        return self.ml.get_pgn()
    #    else:
    #        return "No logger data!"

    def set_board(self, board = None):
        if board == None:
            self.board = chess.Board()
        else:
            self.board = board

    def get_board(self):
        return self.board
    
    def setup_from_fen(self, fen):
        self.board.set_fen(fen)

    def make_move(self, move):
        self.board.push(move)

    def evaluate_move(self, move):
        return 0
    
    def get_move_list(self, evaluated = False):
        legal_moves = list(self.board.legal_moves)
        # Sort the Move List to optimize MinMax
        if evaluated:
            legal_moves.sort(key=lambda move: self.evaluate_move(move), reverse=True)
        return legal_moves
    
    def make_move(self, move):
        new_board = self.board.copy()
        new_board.push(move)
        return new_board

    def evaluate_game_over(self):
        if self.board.is_checkmate():
            logging.debug(f"Mate, Turn: {self.board.turn}")
            if self.board.turn == chess.BLACK:
                score = self.CHECKMATE_VALUE
            else:
                score = -self.CHECKMATE_VALUE
            return score
        return self.DRAW_VALUE
        
    def get_best_move(self):
        if self.board.is_game_over():
            return self.evaluate_game_over(), None, None
        return None, None, None

    def cleanup(self):
        pass
