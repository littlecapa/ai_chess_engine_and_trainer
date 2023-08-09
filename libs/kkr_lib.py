import chess
import random
import logging
from chess_lib import uci_to_square, generate_random_square, get_empty_board


def set_kkr_position(white_king_position, black_king_position, white_rook_position):
    logging.info(f"Positions: {white_king_position}, {black_king_position}, {white_rook_position}")
    # Create a chess board
    board = get_empty_board()
    piece = chess.Piece(chess.KING, chess.WHITE)
    square = uci_to_square(white_king_position)
    # Position the piece on the board
    board.set_piece_at(square, piece)
    logging.info(f"Fen: {board.fen()}")
    piece = chess.Piece(chess.KING, chess.BLACK)
    square = uci_to_square(black_king_position)
    # Position the piece on the board
    board.set_piece_at(square, piece)
    piece = chess.Piece(chess.ROOK, chess.WHITE)
    logging.info(f"Fen: {board.fen()}")
    square = uci_to_square(white_rook_position)
    # Position the piece on the board
    board.set_piece_at(square, piece)
    logging.info(f"Fen: {board.fen()}")
    if board.is_valid():
        return board
    logging.info(f"Invalid Position: {white_king_position}, {black_king_position}, {white_rook_position}")
    return None
    
def set_random_kkr_position():
    while True:
        pos = [None] * 3
        for i in range(3):
            pos[i] = generate_random_square()
        logging.info(f"Position: {pos}")
        board = set_kkr_position(pos[0], pos[1], pos[2])
        if board is not None:
            return board
        logging.info(f"Invalid Position: {pos}")
