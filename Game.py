import time 
from Player import humanPlayer , randomComputerPlayer
class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)] #a list to represent a 3*3 board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3]for i in range(3)]:
            print(' '+' | '.join(row) + ' | ')    

    @staticmethod
    def print_board_nums():
        # to tell us what number is in which board 
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(" "+" | ".join(row)+" |   ")        
    def winner(self,square,letter):
        row_in = square // 3
        row = self.board[row_in*3 : (row_in + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_in = square % 3
        column = [self.board[col_in+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True 

        if square % 2 == 0 : 
            diagnol1 = [self.board[i] for i in [0,4,8]]
            if all(spot == letter for spot in diagnol1):
                return True
            diagnol2 = [self.board[i] for i in [2,4,6]]
            if all(spot == letter for spot in diagnol2):
                return True        
        return False

    def available_moves(self):
        return[i for i, spot in enumerate(self.board) if spot == ' ']        
    def empty_squares(self):
        return " " in self.board
    def num_empty_squares(self):
        return self.board.count(" ")
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter 
            return True 
        return False 

def play(game, o_player, x_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X"  # That's the starting letter
    while game.empty_squares():
        if letter == "O":
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            letter = "O" if letter == "X" else "X"

        time.sleep(2.0)

    if print_game:
        print("It's a tie!")

if __name__ == "__main__":
    x_player = humanPlayer("X")
    o_player = randomComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
