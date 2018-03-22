import sys
board = ['0','1','2','3','4','5','6','7','8']
#board check is to watch length if board_check lenth == 9 game = tie
board_check = []
#mainPlayer
class Player1(object):
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

#second player
class Player2(object):
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
    def change_name(self, name):
        self.name = name
    def show_name(self):
        print('player2 name: ' + self.name + ' player2 piece: ' + self.piece)

#boolean for gamePlaying
gamePlaying = True
#create players but start_game will modify players...
player1 = Player1('player1', 'X')
player2 = Player2('player2', 'O')

#function to change player1 attributes
def start_player1():
    change = raw_input('Player1 do you wish to change Name or Piece? yes or no?').lower()
    if change == 'yes':
        result = raw_input('Enter new Name: ')
        player1.change_name(result)
        result1 = raw_input('Enter piece you wish to be "X" or "O".').upper()
        if result1 == 'X':
            player1.change_piece(result1)
            player2.piece = 'O'
            player1.show_name()
            return start_player2()
        elif result1 == 'O':
            player1.change_piece(result1)
            player2.piece = 'X'
            player1.show_name()
            return start_player2()
    elif change == 'no':
        player1.show_name()
        return start_player2()
    else:
        print('Command not recognized...')
        return start_player1()

#function to change player2 attributes but only player1 gets to pick X or O...
def start_player2():
    change = raw_input('player2 do you wish to change name? yes or no').lower()
    if change == 'yes':
        result = raw_input('Enter new Name')
        player2.change_name(result)
        player2.show_name()
        return play_again()
    elif change == 'no':
        player2.show_name()
        return play_again()
    else:
        print('Command not recognized...')
        return start_player2()

def print_board():
    print(' {} | {} | {}'.format(board[0], board[1], board[2]))
    print('_____________')
    print(' {} | {} | {} '.format(board[3], board[4], board[5]))
    print('_____________')
    print(' {} | {} | {}'.format(board[6], board[7], board[8]))
    player_move()

def player_move():
    if gamePlaying:
        if player1.turn:
            print(player1.name + ' pick a number to make your move')
            move = int(raw_input("Spot number: "))
            if move >= 9:
                print('Number Not on board..')
                return player_move()
            if board[move] == 'X' or board[move] == 'O':
                print('That Spot is Taken')
                return player_move()
            else :
                board[move] = player1.piece
                board_check.append(player1.piece)
                player1.turn = False
                return check_win(player1.piece, player1.name)
        if not player1.turn:
            print(player2.name + ' pick a number to make your move')
            move2 = int(raw_input("Spot number: "))
            if move2 >= 9:
                print('Number Not on board')
                return player_move()
            if board[move2] == 'X' or board[move2] == 'O':
                print('That Spot is taken')
                return player_move()
            else:
                board[move2] = player2.piece
                board_check.append(player2.piece)
                player1.turn = True
                return check_win(player2.piece, player2.name)

#propbably should have made one if statment with all winning blocks.....
def check_win(marker, playername):
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
start_player1()
