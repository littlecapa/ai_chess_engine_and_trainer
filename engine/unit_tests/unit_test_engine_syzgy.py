import sys
sys.path.append('..')
import unittest
from chess_engine_syzygy import ChessEngineSyzygy
import logging

class Tests_Engine_SYZYGY(unittest.TestCase):
    
    def __init__(self, methodName='runTest', custom_arg=None):
        super().__init__(methodName)
        print("Setup")
        self.engine = ChessEngineSyzygy()

    def test_setup_from_fen(self):
        fen_str = "R7/1K6/8/8/8/8/8/7k w - - 0 1"
        self.engine.setup_from_fen(fen_str)
        print(self.engine.get_best_move())

        fen_str = "R7/1K6/8/8/8/8/8/7k b - - 0 1"
        self.engine.setup_from_fen(fen_str)
        print(self.engine.get_best_move())
 
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

