import unittest
from engine.chess_engine_syzygy import ChessEngineSyzygy
from libs.log_lib import setup_logging
import logging
from chess import Move

class Tests_Engine_SYZYGY(unittest.TestCase):
    
    def __init__(self, methodName='runTest', custom_arg=None):
        super().__init__(methodName)
        self.engine = ChessEngineSyzygy()

    def test_setup_from_fen(self):
        fen_str = "R7/1K6/8/8/8/8/8/7k w - - 0 1"
        self.engine.setup_from_fen(fen_str)
        eval, move, best_distance = self.engine.get_best_move()
        self.assertEqual(eval, 10700.0)
        self.assertEqual(move.uci(), "a8g8")
        self.assertEqual(best_distance, 19)
        # Flip Color
        
        fen_str = "R7/1K6/8/8/8/8/8/7k b - - 0 1"
        self.engine.setup_from_fen(fen_str)
        eval, move, best_distance = self.engine.get_best_move()
        self.assertEqual(eval, -10200.0)
        self.assertEqual(move.uci(), "h1g2")
        self.assertEqual(best_distance, -24)

if __name__ == '__main__':
    setup_logging()
    logging.info("Start Tests")
    unittest.main()
    logging.info("End Tests")

