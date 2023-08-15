import unittest
from bitboards.bit_board import Bitboard
import logging
from libs.log_lib import setup_logging
from libs.chess_lib import uci_to_bb_square


class Tests_Basic_Bitboard(unittest.TestCase):

    def test_uci_to_square(self):
        bb = Bitboard()
        fen_with_en_passant = "rnbqkbnr/ppppp2p/5p2/5p2/8/8/PPPPPPPP/RNBQKBNR w KQkq f6 0 3"
        bb.setup_from_fen(fen_with_en_passant)
        index = bb.__repr__().find("White EP: f6 KQkq")
        self.assertGreater(index, 0)

    def test_get_832xbool_vector(self):
        bb = Bitboard()
        fen_with_en_passant = "rnbqkbnr/ppppp2p/5p2/5p2/8/8/PPPPPPPP/RNBQKBNR w KQkq f6 0 3"
        bb.setup_from_fen(fen_with_en_passant)
        repr_str = bb.__repr__()
        bool_vector = bb.get_13_63_bool_vector()
        bb.set_13_63_bool_vector(bool_vector)
        self.assertEqual(repr_str, bb.__repr__())

    def test_setup_from_fen(self):
        bb = Bitboard()
        fen_e4e5nf3nc6d4 = "r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq d3 0 1"
        bb.setup_from_fen(fen_e4e5nf3nc6d4)
        bit_board = bb.get_bitboard()
        rank, file = uci_to_bb_square("f2")
        self.assertEqual(bit_board[0][rank][file], 1)
        rank, file = uci_to_bb_square("d7")
        self.assertEqual(bit_board[6][rank][file], 1)
        rank, file = uci_to_bb_square("e7")
        self.assertEqual(bit_board[6][rank][file], 0)
        # Knights
        rank, file = uci_to_bb_square("b1")
        self.assertEqual(bit_board[1][rank][file], 1)
        rank, file = uci_to_bb_square("c6")
        self.assertEqual(bit_board[7][rank][file], 1)
        # Bishops
        rank, file = uci_to_bb_square("c1")
        self.assertEqual(bit_board[2][rank][file], 1)
        rank, file = uci_to_bb_square("f8")
        self.assertEqual(bit_board[8][rank][file], 1)
        # Rooks
        rank, file = uci_to_bb_square("a1")
        self.assertEqual(bit_board[3][rank][file], 1)
        rank, file = uci_to_bb_square("h8")
        self.assertEqual(bit_board[9][rank][file], 1)
        # Queens
        rank, file = uci_to_bb_square("d1")
        self.assertEqual(bit_board[4][rank][file], 1)
        rank, file = uci_to_bb_square("d8")
        self.assertEqual(bit_board[10][rank][file], 1)
        # Kings
        rank, file = uci_to_bb_square("e1")
        self.assertEqual(bit_board[5][rank][file], 1)
        rank, file = uci_to_bb_square("e8")
        self.assertEqual(bit_board[11][rank][file], 1)

if __name__ == '__main__':
    setup_logging()
    logging.info("Start Tests")
    unittest.main()
    logging.info("End Tests")

