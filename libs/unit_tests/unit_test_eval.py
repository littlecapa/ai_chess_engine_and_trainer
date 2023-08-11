import unittest
from libs.eval_lib import get_evaluation, is_forced_mate, is_mate, get_is_mate_value, get_mate_in_one_value
from libs.log_lib import setup_logging
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

    tests_mate = [0, 1, 2, 3, 4, 52, 51, 50, 49, 18, 17, 16, 15, +22, -1, -2, -50, -51, -52, 98, 99, 100, 101, 102]
    tests_mate_results = [0.0, get_is_mate_value(), get_mate_in_one_value(), 12300, 12200, 7400, 7500, 7600, 7700, 10800, 10900, 11000, 11100, 10400, -get_is_mate_value(), -12500, -7600, -7500, -7400, 2800, 2700, 2600, 2500, 2500]

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

    def test_is_mate(self):
        for index, test in enumerate(self.tests_forced_mate):
            result = is_mate(test*5)
            self.assertEqual(result, self.tests_forced_mate_results[index])
            result = is_mate(-test*5)
            self.assertEqual(result, self.tests_forced_mate_results[index])

if __name__ == '__main__':
    setup_logging()
    logging.info("Start Tests")
    unittest.main()
    logging.info("End Tests")

