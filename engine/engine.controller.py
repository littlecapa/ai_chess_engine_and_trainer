from engine.ChessEngine_v8 import ChessEngine_v8
from models.net_KRk import KRk_Net_ChatGPT
import os
import logging
import torch

def load_checkpoint(model, file):
    checkpoint = torch.load(file)
    model.load_state_dict(checkpoint['state_dict'])

if __name__ == "__main__":
    # Step 1: Setup Initial Position
    #start_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    start_position = "8/8/8/8/8/2k5/1R6/K7 w - - 0 1"
    initial_position = start_position
    max_depth = 3  # Adjust the maximum search depth

    eval_net = KRk_Net_ChatGPT(num_channels = 13*64, dropout_rate = 0.0).cuda()
    load_checkpoint(model = eval_net, file = "C:/Users/littl/Documents/GIT/AI/ai_chess_engine_and_trainer/models/checkpoints/best.pth.tar")
    chess_engine = ChessEngine_v8(eval_net, initial_position, max_depth)
    board = chess_engine.board

    while not board.is_game_over():
        # Step 2: Computer finds the best move
        best_move, value = chess_engine.find_best_move()

        # Step 3: Move is executed on the board
        board.push(best_move)

        # Step 4: Disply Board
        print(board)

        # Step 5: User enters a move
        user_move = input("Enter your move (e.g., 'e2e4'): ")

        # Step 6: Move is executed on the board
        try:
            board.push_san(user_move)
        except ValueError:
            print("Invalid move. Please try again.")
            continue

    # Step 7: Game is over
    print("Game over. Result: " + board.result())