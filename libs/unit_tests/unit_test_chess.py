import unittest
from libs.chess_lib import uci_to_square, rank_file_from_square, str_square_from_rank_file, get_zero_bit_vector, turn_and_en_passant_square_bits_to_str, turn_and_en_passant_square_to_bits
from libs.log_lib import setup_logging
import logging
import chess

class Tests_Eval_Mate(unittest.TestCase):

    def test_uci_to_square(self):
        self.assertEqual(uci_to_square("a1"), 0)
        self.assertEqual(uci_to_square("a8"), 63-7)
        self.assertEqual(uci_to_square("h1"), 7)
        self.assertEqual(uci_to_square("h8"),63)
        self.assertEqual(uci_to_square("d4"), 27)
        self.assertEqual(uci_to_square("d5"), 35)
        self.assertEqual(uci_to_square("e4"), 28)
        self.assertEqual(uci_to_square("e5"), 36)

    def test_square_from_rank_file(self):
        self.assertEqual(str_square_from_rank_file(0,0), "a1")
        self.assertEqual(str_square_from_rank_file(7,7), "h8")
        self.assertEqual(str_square_from_rank_file(4,3), "d5")
        self.assertEqual(str_square_from_rank_file(3,4), "e4")

    def test_turn_and_en_passant_square_bits_to_str(self):
        bit_vector = get_zero_bit_vector()
        self.assertEqual(turn_and_en_passant_square_bits_to_str(bit_vector), "Black ")
        bit_vector[0] = 1
        self.assertEqual(turn_and_en_passant_square_bits_to_str(bit_vector), "White ")
        bit_vector[1] = 1
        self.assertEqual(turn_and_en_passant_square_bits_to_str(bit_vector), "White EP: a6")
        bit_vector[4] = 1
        self.assertEqual(turn_and_en_passant_square_bits_to_str(bit_vector), "White EP: b6")
        bit_vector[3] = 1
        self.assertEqual(turn_and_en_passant_square_bits_to_str(bit_vector), "White EP: d6")
        bit_vector[0] = 0
        self.assertEqual(turn_and_en_passant_square_bits_to_str(bit_vector), "Black EP: d3")
        bit_vector[2] = 1
        self.assertEqual(turn_and_en_passant_square_bits_to_str(bit_vector), "Black EP: h3")

    def test_turn_and_en_passant_square_to_bits(self):
        fen_with_en_passant = "rnbqkbnr/ppppp2p/5p2/5p2/8/8/PPPPPPPP/RNBQKBNR w KQkq f6 0 3"
        board = chess.Board(fen=fen_with_en_passant)
        bit_vector = turn_and_en_passant_square_to_bits(board)
        self.assertEqual(turn_and_en_passant_square_bits_to_str(bit_vector), "White EP: f6")
        fen_with_en_passant = "rnbqkbnr/ppppp1pp/5p2/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 3"
        board = chess.Board(fen=fen_with_en_passant)
        bit_vector = turn_and_en_passant_square_to_bits(board)
        self.assertEqual(turn_and_en_passant_square_bits_to_str(bit_vector), "Black EP: e3")

    def test_get_rank_file(self):
        square = uci_to_square("a1")
        rank, file = rank_file_from_square(square)
        self.assertEqual(rank, 0)
        self.assertEqual(file, 0)
        square = uci_to_square("h8")
        rank, file = rank_file_from_square(square)
        self.assertEqual(rank, 7)
        self.assertEqual(file, 7)
        square = uci_to_square("d5")
        rank, file = rank_file_from_square(square)
        self.assertEqual(rank, 4)
        self.assertEqual(file, 3)
        square = uci_to_square("e4")
        rank, file = rank_file_from_square(square)
        self.assertEqual(rank, 3)
        self.assertEqual(file, 4)
        square = uci_to_square("b8")
        rank, file = rank_file_from_square(square)
        self.assertEqual(rank, 7)
        self.assertEqual(file, 1)
        square = uci_to_square("g1")
        rank, file = rank_file_from_square(square)
        self.assertEqual(rank, 0)
        self.assertEqual(file, 6)
        square = uci_to_square("f8")
        rank, file = rank_file_from_square(square)
        self.assertEqual(rank, 7)
        self.assertEqual(file, 5)
        square = uci_to_square("b3")
        rank, file = rank_file_from_square(square)
        self.assertEqual(rank, 2)
        self.assertEqual(file, 1)
        
if __name__ == '__main__':
    setup_logging()
    logging.info("Start Tests")
    unittest.main()
    logging.info("End Tests")

