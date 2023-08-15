import unittest
from trainer.trainer_data_loader import Data_Loader
from collector.loader_info import get_out_dir_annotated_positions

import logging
from libs.log_lib import setup_logging
import os
import torch


class Tests_DataLoader(unittest.TestCase):

    Testdata_Filename = "fen_eval_KRk_2023_08_11_11_21_08.csv"

    def test_lload(self):
        test_dataset = Data_Loader(os.path.join(get_out_dir_annotated_positions(), self.Testdata_Filename))
        loader = torch.utils.data.DataLoader(test_dataset, batch_size=1, shuffle=False)
        self.assertEqual(len(loader), 18382)
        for pos, eval, mate in loader:
            self.assertEqual(torch.tensor([11500.], dtype=torch.float64), eval)
            self.assertEqual(torch.tensor([11]), mate)
            break
    
if __name__ == '__main__':
    setup_logging()
    logging.info("Start Tests")
    unittest.main()
    logging.info("End Tests")

