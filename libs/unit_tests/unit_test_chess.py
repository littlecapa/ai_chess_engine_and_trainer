import sys
sys.path.append('..')
import unittest
from chess_lib import uci_to_square
from log_lib import setup_logging
import logging

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
        
if __name__ == '__main__':
    setup_logging()
    logging.info("Start Tests")
    unittest.main()
    logging.info("End Tests")

