import sys
sys.path.append('..')
import unittest
from kkr_lib import set_kkr_position, set_random_kkr_position
import logging
import chess

class Tests_Eval_Mate(unittest.TestCase):

    def test_kkr_position(self):
        board = set_kkr_position("a1", "c3", "b2")
        self.assertEqual(board.is_valid(), True)

        board = set_kkr_position("a1", "b2", "c3")
        self.assertEqual(board, None)

    def test_random_kkr_position(self):
        board = set_random_kkr_position()
        self.assertEqual(board.is_valid(), True)

        
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

