import chess
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