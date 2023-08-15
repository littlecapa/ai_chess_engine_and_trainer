import unittest
from trainer.trainer import Chess_Trainer
from collector.loader_info import get_out_dir_annotated_positions
import torch
import logging
from libs.log_lib import setup_logging
import os

class Tests_DataLoader(unittest.TestCase):

    Testdata_Filename = "fen_eval_KRk_2023_08_11_11_21_08.csv"

    def check_env(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        logging.info(f"Torch Device: {device}")

    def test_first_training(self):
        self.check_env()
        first_training = True
        trainer = Chess_Trainer( train_data_file = os.path.join(get_out_dir_annotated_positions(), self.Testdata_Filename),  first_training = first_training, filename = "chess.h5", learning_rate = 1e-2)
        trainer.do_training(batch_size = 1, train_size = 0.8, num_epochs = 2, shuffle = False)

if __name__ == '__main__':
    setup_logging()
    logging.info("Start Tests")
    unittest.main()
    logging.info("End Tests")

