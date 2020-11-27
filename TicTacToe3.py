from IPython.display import clear_output

def display_board(board):  
    clear_output() 
    print("   |   |")
    print(" " + board[7] + " | "+board[8]+" | "+board[9])
    print("   |   |")
    print("-----------")  
    print("   |   |")
    print(" "+board[4]+" | "+board[5]+" | "+board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" "+board[1]+" | "+board[2]+" | "+board[3])
    print("   |   |")

def place_marker(board, marker, position):
    
    board[position]=marker


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 


def space_check(board, position):
    
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower()


def computer_choice(board, n, sign, comp):
    place = 0

    if n==1:
        place = 3

    elif n==3:
        if sign==board[9] or sign==board[6] or sign==board[8]:
            place = 1
        elif sign==board[5]:
            place = 7
        else:
            place = 9

    elif n==5:

        if ( sign==board[9] or sign==board[6] ) and comp==board[1]:

            if sign==board[2]:
                place = 7

            else:
                place = 2

        elif sign==board[7] and comp==board[9]:

            if sign==board[6]:
                place = 1

            else:
                place = 6

        elif sign==board[5] and comp==board[7]:

            if sign==board[9]:
                place = 1

            elif sign==board[1]:
                place = 9
           
            elif sign==board[2]:
                place = 8
                  
            elif sign==board[4]:
                place = 6
                 
            elif sign==board[8]:
                place = 2
                  
            elif sign==board[6]:
                place = 4

        elif sign==board[4] and comp==board[9]:

            if sign==board[6]:
                place = 5

            else:
                place = 6

        elif sign==board[4] and comp==board[9]:

            if sign==board[6]:
                place = 5
            else:
                place = 6

        elif sign==board[8] or comp==board[1]:

            if sign==board[2]:
                place = 5
            else:
                place = 2

        elif sign==board[1] or sign==board[2]:

            if sign==board[6]:
                place = 7
            else:
                place = 6


    elif n==7:

        if ( sign==board[9] and sign==board[2] ) or ( sign==board[6] and sign==board[2] ):

            if sign==board[5]:
                place = 4
                   
            elif sign==board[4]:
                place = 5
            
            else:
                place = 4

        elif sign==board[7] and comp==board[9] and sign==board[6] and comp==board[1]:  

            if sign==board[2]:
                place = 5
                   
            elif sign==board[5]:
                place = 2
            
            else:
                place = 2

        elif sign==board[4] and comp==board[9] and sign==board[6] and comp==board[5]:


            if sign==board[1]:
                place = 7
                
            elif sign==board[7]:
                place = 1
                
            else:
                place = 1

        elif ( sign==board[1] and sign==board[6] ) or ( sign==board[2] and sign==board[6] ):

            if sign==board[5]:
                place = 8
                  
            elif sign==board[8]:
                place = 5

            else:
                place = 5

        elif sign==board[8] and comp==board[1] and sign==board[2] and comp==board[5]:

            if sign==board[7]:
                place = 9
            
            elif sign==board[9]:
                place = 7

            else:
                place = 9

        elif sign==board[5] and comp==board[7] and sign==board[9] and comp==board[1]:

            if sign==board[2]:
                place = 4
                    
            elif sign==board[4]:
                place = 2

            else:
                place = 4

        elif sign==board[5] and comp==board[7] and sign==board[1] and comp==board[9]:

            if sign==board[8]:
                place = 6
            elif sign==board[6]:
                place = 8
            else:
                place = 6

        elif ( sign==board[5] and sign==board[2] ) or ( sign==board[5] and sign==board[4] ):
            if sign==board[9]:
                place = 1
            else:
                place = 9

        elif ( sign==board[5] and sign==board[8] ) or ( sign==board[5] and sign==board[6] ):

            if sign==board[1]:
                place = 9
            else:
                place = 1

    elif n==9:

        if ( sign==board[5] and comp==board[7] and sign==board[2] and comp==board[8] ) or ( sign==board[5] and comp==board[7] and sign==board[8] and comp==board[2] ) :

            if sign==board[9] and comp==board[1]:
                if sign==board[4]:
                    place = 6
                else:
                    place = 4

            elif sign==board[1] and comp==board[9]:
                if sign==board[6]:
                    place = 4
                else:
                    place = 6
        elif( sign==board[5] and comp==board[7] and sign==board[4] and comp==board[6] ) or ( sign==board[5] and comp==board[7] and sign==board[6] and comp==board[4] ):

            if sign==board[9] and comp==board[1]:
                if sign==board[2]:
                    place = 8
                else:
                    place = 2

            elif sign==board[1] and comp==board[9]:
                if sign==board[8]:
                    place = 2
                else:
                    place = 8
    return place


print("Let's play Tic Tac Toe")

while True:

    theBoard = [' '] * 10
    computer_marker = "X"
    player_marker = "O"
    turn = "computer"
    print(turn + ' will go first & chooses X to play')
    rounds = 1
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == "computer":
    
            display_board(theBoard)

            position = computer_choice(theBoard,rounds,player_marker,computer_marker) 
            rounds = rounds+1
            
            place_marker(theBoard, computer_marker, position)
            
            if win_check(theBoard, computer_marker):
                display_board(theBoard)
                print('Computer has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player'

        else:

            display_board(theBoard)
            position = player_choice(theBoard)
            rounds = rounds+1
            place_marker(theBoard, player_marker, position)

            if win_check(theBoard, player_marker):
                display_board(theBoard)
                print('Congratulations! Player has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'computer'

    if not replay():
        break