import unittest
from libs.tensor_lib import convert_int64_to_int32, convert_int32_to_int64
from libs.log_lib import setup_logging
import torch
import logging

class Tests_Eval_Mate(unittest.TestCase):

    def generate_random_int64_tensor(self, size):
        return torch.randint(torch.iinfo(torch.int64).min, torch.iinfo(torch.int64).max, size=(size,1), dtype=torch.int64).squeeze()

    def test_tensor_convert_64_32_64(self):
        for i in range(100):
            first_int64_tensor = self.generate_random_int64_tensor(13)
            int32_tensor = convert_int64_to_int32(first_int64_tensor)
            second_int64_tensor = convert_int32_to_int64(int32_tensor)
            comparison_result = torch.equal(first_int64_tensor, second_int64_tensor)
            self.assertEqual(comparison_result, True)
        
if __name__ == '__main__':
    setup_logging()
    logging.info("Start Tests")
    unittest.main()
    logging.info("End Tests")

