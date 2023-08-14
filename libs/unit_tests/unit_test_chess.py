import unittest
from libs.chess_lib import uci_to_square, rank_file_from_square
from libs.log_lib import setup_logging
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

