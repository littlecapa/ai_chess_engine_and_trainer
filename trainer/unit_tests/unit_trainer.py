import unittest
from trainer.trainer import Chess_Trainer
from collector.loader_info import get_KRk_training_data_file
import torch
import logging
from libs.log_lib import setup_logging
import os

class Tests_DataLoader(unittest.TestCase):

    
    def check_env(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        logging.info(f"Torch Device: {device}")

    def test_first_training(self):
        self.check_env()
        first_training = True
        train_data_file = get_KRk_training_data_file(k = 10)
        trainer = Chess_Trainer( train_data_file = train_data_file,  first_training = first_training, filename = "chess.h5", learning_rate = 1e-2)
        trainer.do_training(batch_size = 1, train_size = 0.9, num_epochs = 10, shuffle = True)

if __name__ == '__main__':
    setup_logging()
    logging.info("Start Tests")
    unittest.main()
    logging.info("End Tests")

