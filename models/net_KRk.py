"""Defines the neural network, losss function and metrics"""
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import logging
import chess

class KRk_Net_ChatGPT(nn.Module):
    
    def __init__(self, num_channels, dropout_rate):
        super(KRk_Net_ChatGPT, self).__init__()

        self.num_channels = num_channels
        self.dropout_rate = dropout_rate

        self.fc1 = nn.Linear(self.num_channels, 256)  # Input layer to hidden layer
        self.fc2 = nn.Linear(256, 128)  # Hidden layer to hidden layer
        self.fc3 = nn.Linear(128, 32)   # Hidden layer to output layer

        self.dropout = nn.Dropout(self.dropout_rate)  # Dropout layer
        self.training = False

    def forward(self, x):
        x = x.float()
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        batch_size = x.size(0)
        training_with_dropout = self.training and batch_size > 1 and self.dropout_rate > 0.0
        if training_with_dropout:
            x = self.dropout(x)
        x = self.fc3(x)
        x = F.log_softmax(x, dim=-1)
        return x
    
    def get_eval(self, board):
        bb = self.get_bb_from_chess_board(board)
        input = self.get_13_64_bool_vector(bb)
        x = self.forward(torch.tensor(input).cuda())
        x = torch.argmax(x, dim=-1)
        return 100 - x if x >= 0 else -100 + x
    
    def get_13_64_bool_vector(self, bb):
        return bb.reshape(-1)
    
    def setup_empty_bitboard(self):
        bitboard = np.zeros((13, 8, 8), dtype=bool)
        return bitboard

    def get_bb_from_chess_board(self, board):
        bitboard = self.setup_empty_bitboard()
        # Iterate over the board and update the bitboard
        for rank in range(8):
            for file in range(8):
                #square = chess.square(file, 7 - rank)
                square = chess.square(file, rank)
                piece = board.piece_at(square)

                # piece_type: An enumeration representing the type of the chess piece (PAWN, KNIGHT, BISHOP, ROOK, QUEEN, or KING).

                if piece is not None:
                    piece_type = piece.piece_type - 1
                    if piece.color == chess.BLACK:
                        piece_type += 6
                    bitboard[piece_type][rank][file] = True

        # Encode the castling rights
        if board.castling_rights & chess.BB_H1:
            bitboard[12][0][0] = True
        if board.castling_rights & chess.BB_A1:
            bitboard[12][0][1] = True
        if board.castling_rights & chess.BB_H8:
            bitboard[12][0][2] = True
        if board.castling_rights & chess.BB_A8:
            bitboard[12][0][3] = True

        # Encode turn and enp passant
        bitboard[12][1] = self.turn_and_en_passant_square_to_bits(board)
        return bitboard

    def turn_and_en_passant_square_to_bits(self, board):
        bit_vector = self.get_zero_bit_vector(8)
        bit_vector[0] = board.turn    
        en_passant_square = board.ep_square
        if en_passant_square is not None:
            bit_vector[1] = 1
            _, file = self.rank_file_from_square(en_passant_square)
            bit_vector = self.int_to_3bit_vector(file, bit_vector, 2)
        return bit_vector
    
    def get_zero_bit_vector(self, length = 8):
        return np.zeros(length, dtype=bool)
    
    def rank_file_from_square(self, square):
        # Split the square into rank and file
        rank = chess.square_rank(square)
        file = chess.square_file(square)
        return rank, file
    
    def int_to_3bit_vector(self, n, vector, start):
        for i in range(start + 2, start-1, -1):  # Loop from the most significant bit to the least significant bit
            vector[i] = n & 1
            n >>= 1
        return vector
    
