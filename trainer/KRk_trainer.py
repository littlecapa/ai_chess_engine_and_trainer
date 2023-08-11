from libs.kkr_lib import set_random_kkr_position
from engine.chess_engine_syzygy import ChessEngineSyzygy
from libs.log_lib import setup_logging
from collector.loader_info import get_out_dir_annotated_positions
from collector.fen_eval_collector import FEN_Eval_Collector

import chess
import logging

def main(collector, white, black):
    board = set_random_kkr_position()
    logging.info(board.fen())
    white.set_board(board)
    black.set_board(board)
    while True:
        if board.turn == chess.WHITE:
            eval, move, mate = white.get_best_move()
        else:
            eval, move, mate = black.get_best_move()
        collector.write_pos(board.fen(), eval, mate)
        logging.debug(f"EVAL: {eval}, {move}, {mate}")
        board.push(move)
        logging.debug(board.fen())
        if board.is_game_over():
            break

    for i, move in enumerate(board.move_stack):
        move_number = (i // 2) + 1
        if i % 2 == 0:
            logging.debug(f"{move_number}. {move}")
        else:
            logging.debug(f"    {move}")

nr_games = 1000

if __name__ == '__main__':
    setup_logging()
    logging.info("Start Training")
    collector = FEN_Eval_Collector(file_path = get_out_dir_annotated_positions(), file_info="KRk")
    white = ChessEngineSyzygy()
    black = ChessEngineSyzygy()
    for i in range(nr_games):
        logging.info(f"Start Training Game {i+1}")
        main(collector, white, black)
        logging.info(f"End Training Game {i+1}")
    logging.info("End Training")