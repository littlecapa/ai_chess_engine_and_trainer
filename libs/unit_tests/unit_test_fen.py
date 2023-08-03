import sys
sys.path.append('..')
import unittest
from fen_lib import split_fen, flip_color_position, flip_color_to_move, flip_castling_options, flip_en_passant_square, flip_color
import logging

class Tests_Eval_Mate(unittest.TestCase):

    TEST_FEN = "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq e6 0 3"
    FLIP_POS = "rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR"
    EXPECTED_RESULT_FEN = "rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR b KQkq e3 0 3"

    def test_split_fen_string(self):
        position, color_to_move, castling_options, en_passant_square, halfmove_clock, fullmove_clock = split_fen(self.TEST_FEN)
        self.assertEqual(position, self.TEST_FEN[:51])
        self.assertEqual(color_to_move, self.TEST_FEN[52])
        self.assertEqual(castling_options, self.TEST_FEN[54:58])
        self.assertEqual(en_passant_square, self.TEST_FEN[59:61])
        self.assertEqual(halfmove_clock, 0)
        self.assertEqual(fullmove_clock, 3)

    def test_flip_fen_components(self):
        position, color_to_move, castling_options, en_passant_square, halfmove_clock, fullmove_clock = split_fen(self.TEST_FEN)
        self.assertEqual(flip_color_position(position), self.FLIP_POS)
        self.assertEqual(flip_color_to_move(color_to_move), "b")
        self.assertEqual(flip_color_to_move(flip_color_to_move(color_to_move)), color_to_move)
        self.assertEqual(flip_castling_options(castling_options), "KQkq")
        self.assertEqual(flip_castling_options("KQ--"), "--kq")
        self.assertEqual(flip_castling_options("KQk-"), "K-kq")
        self.assertEqual(flip_en_passant_square(en_passant_square), "e3")
        self.assertEqual(flip_en_passant_square("h8"), "h1")
        self.assertEqual(flip_en_passant_square("a1"), "a8")

    def test_flip_fen(self):
        new_fen = flip_color(self.TEST_FEN)
        self.assertEqual(new_fen, self.EXPECTED_RESULT_FEN)
        new_fen = flip_color(self.TEST_FEN.replace('Q', '-'))
        self.assertEqual(new_fen, self.EXPECTED_RESULT_FEN.replace('q', '-'))
        new_fen = flip_color(self.TEST_FEN.replace('k', '-'))
        self.assertEqual(new_fen, self.EXPECTED_RESULT_FEN.replace('K', '-'))
        
def setup_logging():
    logging.basicConfig(
        filename='app.log',  # Change this to your desired log file path
        level=logging.INFO,  # Change the log level as needed (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='%(asctime)s [%(levelname)s]: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

if __name__ == '__main__':
    setup_logging()
    logging.info("Start Tests")
    unittest.main()
    logging.info("End Tests")

