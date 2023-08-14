import chess
import numpy as np
import logging
import random

def uci_to_square(uci):
    file_index = ord(uci[0]) - ord('a')
    rank_index = int(uci[1]) - 1
    return chess.square(file_index, rank_index)

FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
def generate_random_square():
    random_file = random.choice(FILES)
    random_rank = random.randint(1, 8)
    return random_file + str(random_rank)

# Define an empty FEN string
EMPTY_FEN = "8/8/8/8/8/8/8/8 w - - 0 1"
def get_empty_board():
# Create an empty chess board
    return chess.Board(fen=EMPTY_FEN)

def rank_file_from_square(square):
    # Split the square into rank and file
    rank = chess.square_rank(square)
    file = chess.square_file(square)
    return rank, file

def square_from_rank_file(rank, file):
    return chess.square(file, rank)

def str_square_from_rank_file(rank, file):
    square_index = square_from_rank_file(rank, file)
    return chess.square_name(square_index)

def get_zero_bit_vector(length = 8):
    return np.zeros(length, dtype=bool)

def turn_and_en_passant_square_to_bits(board):
    bit_vector = get_zero_bit_vector(8)
    bit_vector[0] = board.turn    
    en_passant_square = board.ep_square
    if en_passant_square is not None:
        bit_vector[1] = 1
        rank, file = rank_file_from_square(en_passant_square)
        bit_vector = int_to_3bit_vector(file, bit_vector, 2)
    return bit_vector

def int_to_3bit_vector(n, vector, start):
    for i in range(start + 2, start-1, -1):  # Loop from the most significant bit to the least significant bit
        vector[i] = n & 1
        n >>= 1
    return vector
    

def bit_vector_to_int(bit_vector):
    result = 0
    for bit in bit_vector:
        result = (result << 1) | bit
    return result

def turn_and_en_passant_square_bits_to_str(bit_vector):
    if bit_vector[0]:
        string = "White "
    else:
        string = "Black "
    if bit_vector[1] == 1:
        file_bits = bit_vector[2:5]
        file = bit_vector_to_int(file_bits)
        if bit_vector[0] == 1:
            rank = (6-1)
        else:
            rank = (3-1)
        square_index = chess.square(file, rank)
        string += f"EP: {chess.square_name(square_index)}"
    return string
