import chess

class ChessEngine_v8:
    def __init__(self, eval_net, initial_position_fen, max_depth=3, ):
        self.board = chess.Board(initial_position_fen)
        self.max_depth = max_depth
        self.eval_net = eval_net

    def evaluate_position(self):
      if self.board.is_checkmate():
        return float("-inf") if self.board.turn == chess.WHITE else float("inf")
      elif self.board.is_stalemate() or self.board.is_insufficient_material() or self.board.is_seventyfive_moves():
        return 0.0
      return self.eval_net.get_eval(self.board)

    def find_best_move(self):
        best_move = None
        maximize = self.board.turn
        best_value = float("-inf") if maximize else float("inf")
        legal_moves = list(self.board.legal_moves)
        best_move = legal_moves[0]
        for move in legal_moves:
            self.board.push(move)
            # Another Fix!
            value = self.minimax(self.max_depth - 1, not maximize)
            self.board.pop()

            if maximize:
              if value > best_value:
                best_value = value
                best_move = move
            else:
              if value < best_value:
                best_value = value
                best_move = move


        return best_move, best_value

    def minimax(self, depth, maximize):
        if depth == 0 or self.board.is_game_over():
            return self.evaluate_position()

        legal_moves = list(self.board.legal_moves)
        best_value = float("-inf") if maximize else float("inf")

        for move in legal_moves:
            self.board.push(move)
            value = self.minimax(depth - 1, not maximize)
            best_value = max(best_value, value) if maximize else min(best_value, value)
            self.board.pop()

        return best_value