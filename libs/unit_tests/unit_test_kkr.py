import sys
sys.path.append('..')
import unittest
from kkr_lib import set_kkr_position, set_random_kkr_position
from log_lib import setup_logging
import chess
import logging

class Tests_Eval_Mate(unittest.TestCase):

    def test_kkr_position(self):
        board = set_kkr_position("a1", "c3", "b2")
        self.assertEqual(board.is_valid(), True)
        self.assertEqual(board.turn, chess.WHITE)
        board = set_kkr_position("a1", "b2", "c3")
        self.assertEqual(board, None)

    def test_random_kkr_position(self):
        board = set_random_kkr_position()
        self.assertEqual(board.is_valid(), True)
        
if __name__ == '__main__':
    setup_logging()
    logging.info("Start Tests")
    unittest.main()
    logging.info("End Tests")

