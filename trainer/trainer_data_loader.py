import logging
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from bitboards.bit_board_interface import Bitboard_Interface
import numpy as np

class Data_Loader(Dataset):

    def __init__(self, data_path):
        self.pos_fen = []
        self.eval = []
        self.mate = []
        logging.info(f"File: {data_path}")
        self.load_data(data_path)

    def __len__(self):
        logging.info(f"LEN")
        return len(self.eval)

    def __getitem__(self, idx):
        #
        # To Do: Convert FEN to Bitvector!
        #
        logging.info(f"Index: {idx}, {self.pos_fen[idx]}")
        return self.pos_fen[idx], self.eval[idx], self.mate[idx]
    
    def load_data(self, data_path):
        logging.info(f"File: {data_path}")
        with open(data_path, 'r') as file:
            lines = file.readlines()
        logging.info(f"File: {data_path}, Lines: {len(lines)}")
        for line in lines:
            values = line.strip().split(';')
            if self.mate == []:
                logging.info(f"Values: {values} {values[0]}")
            bbi = Bitboard_Interface(fen = values[0])
            self.pos_fen.append(bbi.get_13_63_bool_vector())
            self.eval.append(float(values[1]))
            self.mate.append(int(values[2]))