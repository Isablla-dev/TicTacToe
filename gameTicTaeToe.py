from random import randrange

board = [
        ['-', '-', '-'],
        ['-', 'X', '-'],
        ['-', '-', '-'],
    ]

free_fields = []

game = 'Running'

def display_board(board):
    
    print ("+-------+-------+-------+\n|       |       |       |")
    
    print (f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
    print("|       |       |       |\n+-------+-------+-------+\n|       |       |       |")
    print (f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
    print("|       |       |       |\n+-------+-------+-------+\n|       |       |       |")
    print (f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
    print("|       |       |       |\n+-------+-------+-------+")


    return board

def enter_move(board):
    
    global fields, move

    fields = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    
    try:
        move = int(input("Ingresa tu movimiento: "))
    
        if fields[move - 1] not in free_fields:
            print("Movimiento invalido")
            move = 'Error'
        else:
            if move == 1:
                board [0][0] = 'O'
            elif move == 2:
                board [0][1] = 'O'
            elif move == 3:
                board [0][2] = 'O'
            elif move == 4:
                board [1][0] = 'O'
            elif move == 6:
                board [1][2] = 'O'
            elif move == 7:
                board [2][0] = 'O'
            elif move == 8:
                board [2][1] = 'O'
            elif move == 9:
                board [2][2] = 'O'
    except:
        print("El movimiento no es valido")
        move = 'Error'
        
    return fields, move

def make_list_of_free_fields(board):
    
    free_fields.clear()
    for i in range(3):
        for j in range(3):
            if board [i][j] != 'O' and board [i][j] != 'X':
                free_fields.append((i, j))
    return free_fields

def victory_for(board):
    
    global ganador
    global game
    
    for i in range(3):
        if board[i][0] == board [i][1] == board[i][2] == 'O':
            game = 'win'
            ganador = 'O'
            return game, ganador
        elif board[i][0] == board [i][1] == board[i][2] == 'X':
            game = 'win'
            ganador = 'X'
            return game, ganador

    for j in range(3):
        if board[0][j] == board [1][j] == board[2][j] == 'O':
            game = 'win'
            ganador = 'O'
            return game, ganador
        elif board[0][j] == board [1][j] == board[2][j] == 'X':
            game = 'win'
            ganador = 'X'
            return game, ganador
    
    if board[0][0] == board [1][1] == board[2][2] == 'O':
        game = True
        ganador = 'O'
        return game, ganador
    elif board[0][2] == board [1][1] == board[2][0] == 'O':
        game = 'win'
        ganador = 'O'
        return game, ganador
    elif board[0][0] == board [1][1] == board[2][2] == 'X':
        game = 'win'
        ganador = 'X'
        return game, ganador
    elif board[0][2] == board [1][1] == board[2][0] == 'X':
        game = 'win'
        ganador = 'X'
        return game, ganador
    else:
        ganador = False
        game = 'Running'
        return game, ganador

def draw_move(board,free_fields):
    
    move_auto = free_fields[randrange(len(free_fields))]

    row = move_auto[0]
    col = move_auto[1]

    board[row][col] = 'X'
    
    return board

game, ganador = victory_for(board)


while game == 'Running': 
    display_board(board)
    make_list_of_free_fields(board)
    enter_move(board)
    if move == 'Error':
        while move == 'Error':
            enter_move(board)
    make_list_of_free_fields(board)
    victory_for(board)
    draw_move(board, free_fields)
    make_list_of_free_fields(board)
    if game != 'win':
        victory_for(board)
    if game == 'win':
        display_board(board)
        if ganador == 'O':
            print('!GANASTE¡')
        elif ganador == 'X':
            print ('!GANEE¡')
    elif len(free_fields) == 0:
            display_board(board)
            print('!EMPATE¡')
            break