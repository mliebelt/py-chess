
import chess

def main():
    # Create a new board
    board = chess.Board()

    # Print the initial board state
    print(board)

    print()

    # Make a move
    move = chess.Move.from_uci("e2e4")
    board.push(move)

    # Print the board after the move
    print(board)

if __name__ == "__main__":
    main()
