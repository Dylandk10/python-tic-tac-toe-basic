#This is the same game but with Computer AI playing against you
#I will combine both to work with eachother
import sys
#main board
board = ['0','1','2','3','4','5','6','7','8']
#ai baord
ai_board = [0,1,2,3,4,5,6,7,8]
#board check is to watch length if board_check lenth == 9 game = tie
board_check = []
#mainPlayer
class Player(object):
    turn = True
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
    def change_name(self, name):
        self.name = name
    def change_piece(self, piece):
        self.piece = piece
    def show_name(self):
        print('Player1 name: ' + self.name +' player1 piece: ' + self.piece)

computerMarker = 'O'

gamePlaying = True
#create player then modify..
player = Player('player', 'X')

def change_player_setup():
    change = raw_input("Do you wish to change name?").lower()
    if change == 'yes' or change == 'y':
        result = raw_input("Enter new Name")
        player.change_name(result)
        return print_board()
    elif change == 'no' or change == 'n':
        print_board()
        return player_move()


def print_board():
    print(' {} | {} | {}'.format(board[0], board[1], board[2]))
    print('_____________')
    print(' {} | {} | {} '.format(board[3], board[4], board[5]))
    print('_____________')
    print(' {} | {} | {}'.format(board[6], board[7], board[8]))

def player_move():
    if gamePlaying:
        if player.turn:
            print("Pick number to make tyour move")
            move = int(raw_input('Spot Number: '))
            if move >= 9:
                print('Number not on board...')
                return player_move()
            if board[move] == 'X' or board[move] == 'O':
                print('That spot is taken please pick another spot')
                return player_move()
            else:
                board[move] = player.piece
                board_check.append(player.piece)
                ai_board[move] = player.piece
                check_win(player.piece, player.name)
                return computer_move()

def computer_move():
    if gamePlaying:
        move = check_spot()
        num = int(move)
        board[num] = 'O'
        board_check.append('O')
        ai_board[num] = 'O'
        check_win('O', 'Computer')
        return player_move()

#check spot needs work
def check_spot():
    if len(board_check) == 9:
        return -1
    elif len(board_check) == 1 and isinstance(board[4], basestring):
        return 4
    elif ai_board[0] == ai_board[1] and board[2].isdigit():
        return 2
    elif ai_board[1] == ai_board[2] and board[0].isdigit():
        return 0
    elif ai_board[3] == ai_board[4] and board[5].isdigit():
        return 5
    elif ai_board[4] == ai_board[4] and board[3].isdigit():
        return 3
    elif ai_board[3] == ai_board[5] and board[4].isdigit():
        return 4
    else:
        for x in ai_board:
            print x
            if x == 'X' or x == 'O':
                pass
            else:
                return x

#propbably should have made one if statment with all winning blocks.....
def check_win(marker, playername):
    print(board)
    print(ai_board)
    if len(board_check) == 9:
        print('Its a Tie!!')
        return play_again()
    elif board[0] == board[1] == board[2] == marker:
        print('Game Over player ' + playername + ' Wins!')
        gamePlaying = False
        return play_again()
    elif board[3] == board[4] == board[5] == marker:
        print('Game Over player ' + playername + ' Wins!')
        gamePlaying = False
        return play_again()
    elif board[6] == board[7] == board[8] == marker:
        print('Game Over player ' + playername + ' Wins!')
        gamePlaying = False
        return play_again()
    elif board[0] == board[3] == board[6] == marker:
        print('Game Over player ' + playername + ' Wins!')
        gamePlaying = False
        return play_again()
    elif board[1] == board[4] == board[7] == marker:
        print('Game Over player ' + playername + ' Wins!')
        gamePlaying = False
        return play_again()
    elif board[2] == board[5] == board[8] == marker:
        print('Game Over player ' + playername + ' Wins!')
        gamePlaying = False
        return play_again()
    elif board[0] == board[4] == board[8] == marker:
        print('Game Over' + playername + ' Wins!')
        gamePlaying = False
        return play_again()
    elif board[2] == board[4] == board[6] == marker:
        print('Game Over player ' + playername + ' Wins!')
        gamePlaying = False
        return play_again()
    else:
        return print_board()

def play_again():
    print('Start game? Yes or No')
    result = raw_input("Pick: ").lower()
    if result == 'yes' or result == 'y':
        global board
        global board_check
        board = [0,1,2,3,4,5,6,7,8]
        board_check = []
        return start_game_again()
    elif result == 'no' or result == 'n':
        sys.exit()
    else:
        print('Command not recognized...')
        return play_again()
def start_game_again():
    return print_board()
change_player_setup()
