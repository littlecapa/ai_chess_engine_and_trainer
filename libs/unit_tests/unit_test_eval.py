import sys
sys.path.append('..')
import unittest
from eval_lib import get_evaluation, is_forced_mate
import logging

class Tests_Eval_Mate(unittest.TestCase):

    tests_eval = [-15.0, -15.1, -200.0, -3, 0, 1, 14.9, 15.0, 15.1, 67676767]
    tests_eval_results = [-1500.00, -1504.14, -1726.95, -300.00, 0.00, 100.00, 1490.00, 1500.0, 1504.14, 2283.04]

    def test_eval_evaluation(self):
        for index, test in enumerate(self.tests_eval):
            result = get_evaluation(test,None)
            self.assertEqual(result, self.tests_eval_results[index])
            result = get_evaluation(-test,None)
            self.assertEqual(result, -self.tests_eval_results[index])
            if index == 0:
                result = get_evaluation(test,-4)
                self.assertNotEqual(result, self.tests_eval_results[index])
                result = get_evaluation(test,"")
                self.assertEqual(result, self.tests_eval_results[index])
        result = get_evaluation(None,None)
        self.assertEqual(result, 0.00)
        result = get_evaluation("",None)
        self.assertEqual(result, 0.00)

    tests_mate = [0, 1, 2, 3, 4, 51, 50, 49, 48, 47, 18, 17, 16, 15, +22]
    tests_mate_results = [0.0, 7500, 7400, 7300, 7200, 2500, 2600, 2700, 2800, 2900, 5800, 5900, 6000, 6100, 5400]

    def test_mate_evaluation(self):
        for index, test in enumerate(self.tests_mate):
            result = get_evaluation("", test)
            self.assertEqual(result, self.tests_mate_results[index])
            result = get_evaluation("", -test)
            self.assertEqual(result, -self.tests_mate_results[index])
            if index == 0:
                result = get_evaluation(None, test)
                self.assertEqual(result, self.tests_mate_results[index])

    tests_forced_mate = [2449.99, 2500.0, 2500.1, 0, 1]
    tests_forced_mate_results = [False, True, True,False, False]

    def test_is_forced_mate(self):
        for index, test in enumerate(self.tests_forced_mate):
            result = is_forced_mate(test)
            self.assertEqual(result, self.tests_forced_mate_results[index])
            result = is_forced_mate(-test)
            self.assertEqual(result, self.tests_forced_mate_results[index])
        
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

