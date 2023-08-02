import chess
import chess.syzygy

from chess_engine import ChessEngine

import sys
sys.path.append("/Users/littlecapa/GIT/python/ai_chess_engine_and_trainer/libs")
from eval_lib import get_evaluation
import logging


class ChessEngineSyzygy(ChessEngine):

    def __init__(self):
        super().__init__()
        self.set_engine_parameters()

    def set_engine_parameters(self, SYZYGY_PATH = "/Users/littlecapa/chess/syzygy", max_pieces = 5):
        self.tablebases = chess.syzygy.Tablebase()
        self.tablebases.add_directory(SYZYGY_PATH)
        self.max_pieces = max_pieces 
        
    def get_best_move(self):
        eval, move, shortest_distance = super().get_best_move()
        if eval != None:
            return eval, move, shortest_distance
        # Generate all legal moves
        legal_moves = self.get_move_list(evaluated = False)
        # Initialize variables
        best_move = None
        shortest_distance = float('inf')
        # Iterate through each legal move
        for move in legal_moves:
            # Make the move on a temporary board
            temp_board = self.make_move(move)
            # Probe the table bases to get the distance to mate
            distance = -self.tablebases.probe_dtz(temp_board)
            logging.debug(f"Move: {move}, Distance: {distance}")

            # Check if the distance is shorter than the current best distance
            if distance is not None and distance > 0 and distance < shortest_distance:
                shortest_distance = distance
                best_move = move
                logging.info(f"Move: {best_move}, Distance: {shortest_distance}")
        if distance is None or distance == 0:
            return self.DRAW_VALUE, move[0], 0
        return get_evaluation(None, shortest_distance), best_move, shortest_distance
