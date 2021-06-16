def display(board): #display board
    print(board[6]+'   | '+board[7]+' | '+board[8])
    print('-----------')
    print(board[3]+'   | '+board[4]+' | '+board[5])
    print('-----------')
    print(board[0]+'   | '+board[1]+' | '+board[2])
    print('\n \n \n')
    

#this function will decide players marker
def players_input():
    '''OUTPUT (player1 marker,player2 marker)'''
    marker= ''
    while marker != 'X'and marker != 'O':
        marker = input('player1:choose X or O\n').upper()
        if marker =='X':
           return('X','O')
        else:
            return('O','X')

#at what position player will mark
def place_marker(board,marker,position):
    board[position] = marker

#win condition
def win_check(board,mark):  
    return ((board[0]==board[1]==board[2]==mark) or  
           (board[3]==board[4]==board[5]==mark) or
           (board[6]==board[7]==board[8]==mark) or
           (board[0]==board[3]==board[6]==mark) or
           (board[1]==board[4]==board[7]==mark) or
           (board[2]==board[5]==board[8]==mark) or
           (board[0]==board[4]==board[8]==mark) or
           (board[2]==board[4]==board[6]==mark))
    

#if system has to choose who will play first
import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'player1'
    else:
        return 'player2'
#checking space in board
def space_check(board,position):  
    return board[position] == ''  

#checking board is full or not
def full_board_check(board):
    if '' not in board:
        return True
    else:
        return False

def player_choice(board):
    position = int(input('choose your position: (0-8)'))
    while position not in [0,1,2,3,4,5,6,7,8] or not space_check(board,position):
        position=int(input('choose your position: (0-8)'))

    return position

        

def replay():
    choice = input('play again? enter Yes or no')
    return choice == 'yes' or choice =='y'

print('welcome to tic tac toe game:')

while True:
      my_board = ['']*9
      display(my_board)
     
      player1_marker,player2_marker = players_input()
      turn = choose_first()
      print(turn + 'will go first')

      play_game =input('ready to play? y or n').upper()
      if play_game == 'Y':
          game_on = True
      else:
          game_on = False
      while game_on :
          if turn == 'player1':
              print("player 1 turn")
              display(my_board)
              position = player_choice(my_board)
              print(position)
              place_marker(my_board,player1_marker,position)
              if win_check(my_board,player1_marker):
                 display(my_board)
                 print('player1 has won the game')
                 game_on = False
              else:
                 if full_board_check(my_board):
                    display(my_board)
                    print('tie game!!')
                    game_on = False
                 else:
                     turn = 'player2'
          else:
                print("player 2 turn")
                display(my_board)
                position = player_choice(my_board)
                print(position)
                place_marker(my_board,player2_marker,position)
                if win_check(my_board,player2_marker):
                   display(my_board)
                   print('player2 has won the game')
                   game_on = False
                else:
                    if full_board_check(my_board):
                       display(my_board)
                       print('tie game!!')
                       game_on = False
                    else:
                        turn = 'player1'


      if not replay():
         break
    
       

