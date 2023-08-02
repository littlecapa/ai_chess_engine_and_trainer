import chess
import chess.syzygy

from chess_engine import ChessEngine

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
        eval, move, shortest_distance = super().get_best_move()
        if eval != None:
            return eval, move, shortest_distance
        # Generate all legal moves
        legal_moves = self.get_move_list(evaluated = False)
        # Initialize variables
        best_move = None
        # Iterate through each legal move
        distance_list = []
        for move in legal_moves:
            temp_board = self.make_move(move)
            distance = -self.tablebases.probe_dtz(temp_board)
            distance_list.append(distance)
            logging.info(f"Move: {move}, Distance: {distance}")
        logging.info(f"List: {distance_list}")
        index, best_distance = self.find_best_move(distance_list)
        logging.info(f"Results: {index}, {best_distance}")
        if best_distance != 0:
            eval = get_evaluation(None, best_distance)
        else:
            eval = get_evaluation(0, None)
        return eval, legal_moves[index], best_distance
