import chess
import chess.syzygy

from engine.chess_engine import ChessEngine

import sys
sys.path.append("/Users/littlecapa/GIT/python/ai_chess_engine_and_trainer/libs")
from eval_lib import get_evaluation, get_is_mate_value
import logging


class ChessEngineSyzygy(ChessEngine):

    def __init__(self):
        super().__init__()
        self.set_engine_parameters()

    def set_engine_parameters(self, SYZYGY_PATH = "/Users/littlecapa/chess/syzygy", max_pieces = 5):
        self.tablebases = chess.syzygy.Tablebase()
        self.tablebases.add_directory(SYZYGY_PATH)
        self.max_pieces = max_pieces 

    def distance_to_eval(self, distance):
        if distance != 0:
            return get_evaluation(None, distance)
        else:
            return get_evaluation(0, None)
    
    def position_to_dist(self, board):
        return self.tablebases.probe_dtz(board)

    def position_to_dist_eval(self, board):
        distance = self.position_to_dist(board)
        eval = self.distance_to_eval(self, distance)
        return distance, eval

    def find_best_move(self, eval_list):
        min_pos_index = -1
        min_pos_value = 999
        max_neg_index = -1
        max_neg_value = 0
    
        for i, eval in enumerate(eval_list):
            if eval <= 0:
                if eval < max_neg_value:
                    max_neg_value = eval
                    max_neg_index = i
            else:
                if eval < min_pos_value:
                    min_pos_value = eval
                    min_pos_index = i
        if min_pos_index != -1:
            return min_pos_index, min_pos_value
        else:
            return max_neg_index, max_neg_value
        
    def get_best_move(self):
        # Check, if Game is over
        logging.debug(f"Find best Move in: {self.board.fen()}")
        eval, move, shortest_distance = super().get_best_move()
        if eval != None:
            return eval, move, shortest_distance
        distance = self.tablebases.probe_dtz(self.board)
        logging.debug(f"Distance: {distance}")
        # Generate all legal moves
        legal_moves = self.get_move_list(evaluated = False)
        # Initialize variables
        best_move = None
        for move in legal_moves:
            temp_board = self.make_move(move)
            new_distance = -self.tablebases.probe_dtz(temp_board)
            logging.info(f"New Distance: {distance} {new_distance} {move}")
            if new_distance == distance:
                if abs(new_distance <= 1):
                    best_move = move
                    break
            if (abs(distance)-1) == (abs(new_distance)):
                best_move = move
                break
        if best_move is None:
            logging.debug(f"No best move")
            raise ValueError(f"No best move, {self.board.fen()}")
        eval = self.distance_to_eval(distance)
        return eval, best_move, distance
