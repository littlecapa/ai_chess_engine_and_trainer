import sys
sys.path.append("/Users/littlecapa/GIT/python/ai_chess_engine_and_trainer/")

from libs.kkr_lib import set_random_kkr_position
from engine.chess_engine_syzygy import ChessEngine as syzygy5
from libs.log_lib import setup_logging

import chess
import logging

def main():
    
    board = set_random_kkr_position()
    white = syzygy5()
    white.set_board(board)
    black = syzygy5()
    black.set_board(board)
    while True:
        if board.turn == chess.WHITE:
            eval, move, mate = white.get_best_move()
        else:
            eval, move, mate = black.get_best_move()
        logging.info(eval, move, mate)
        board.push(move)
        logging.debug(board.fen())
        if board.is_game_over():
            break

    for i, move in enumerate(board.move_stack):
        move_number = (i // 2) + 1
        if i % 2 == 0:
            print(f"{move_number}. {move}")
        else:
            print(f"    {move}")
        
if __name__ == '__main__':
    setup_logging()
    main()

