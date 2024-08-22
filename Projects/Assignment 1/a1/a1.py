from typing import Optional
from support import *


def play_game() -> None:
    """
    Pre-condition:
        All functions used in this function are defined

    Get the game played in right display order
        
    Parameters:
        null

    Return:
        None
    """

    #ask for board size input
    board_size = int(input('Enter board size: '))
        
    #ask for ship sizes input and
    #convert the string input into list of integers
    ship_sizes1 = input('Enter ships sizes: ').split(',')
    ship_sizes2 = []
    for ship_size in ship_sizes1:
        ship_sizes2.append(int(ship_size))

    print(DIVIDER_MESSAGE)
        
    #set up board for each player
    print(P1_PLACEMENT_MESSAGE)
    p1_board = setup_board(board_size, ship_sizes2)
    print(P2_PLACEMENT_MESSAGE)
    p2_board = setup_board(board_size, ship_sizes2)
        
    #define a variable for determine whose turn it is
    turns = 1
        
    #repeat making attacks until get the winner
    while get_player_hp(p1_board) != 0 and get_player_hp(p2_board) != 0:
        print(NEXT_TURN_GRAPHIC)
        display_game(p1_board, p2_board, False)
        print('')
        if turns % 2 == 1:
            print('PLAYER 1\'s turn!')
            make_attack(p2_board)
            turns += 1
        else:
            print('PLAYER 2\'s turn!')
            make_attack(p1_board)
            turns += 1

    #game over
    print(GAME_OVER_GRAPHIC)
    print(get_winner(p1_board, p2_board),'won!')
    display_game(p1_board, p2_board, True)
    return
        

def num_hours() -> float:
    """
    Pre-condition:
        Finished the assignment alive

    Get hour spent on assignment 1

    Parameter:
        null

    Return:
        Float shows the hours used for assignment 1
    """

    #get the number used for assignment 1
    hour_used = 55.0
    return hour_used


def create_empty_board(board_size: int) -> list[str]:
    """
    Pre-coditions:
        board_size value must between 2 and 9 inclusive

    Create an empty board for gaming

    Parameter:
        board_size: Length of board sides

    Returns:
        A list contains few strings inside
    """

    #create a long string used for board rows
    board_rows = EMPTY_SQUARE * board_size
        
    #set up a initial value for 'order of colomns' shows
    #where row located
    order_of_colomns = 1
    #set up a initial value for list 'board'
    board = [board_rows]
        
    #set up a loop for creating the 'board'
    while order_of_colomns < board_size:
        board.append(board_rows)
        order_of_colomns += 1
    return board


def get_square(board: list[str], position: tuple[int,int]) ->str:
    """
    Pre-conditions:
        position must exist on board

    Get the element shows in board in a specific position

    Parameter:
        board: Board used for searching element
        position: Position of element to be searched

    Returns:
        A string shows the element find in that position
    """

    #get the first int in tuple 'position' th string in list
    #'board' and get the second int in tuple 'position' th
    #element in string 'board_rows'
    square_get = board[position[0]][position[1]]
    return square_get


def change_square(board: list[str], position: tuple[int,int],
                  new_square: str) -> None:
    """
    Pre-conditions:
        position must exit on the board

    Change the element found with a specific element
        
    Parameter:
        board: Board used for searching element
        position: Position of element to be searched
        new_square: The element used for substitution

    Returns:
        None
    """

    #get the row going to be changed
    row_get = board[position[0]]
        
    #sub the new square in and remove the old one
    row_changed = (row_get[0:position[1]] +
                   new_square + row_get[(position[1]+1):])
        
    #put the changed row back into the board
    board[position[0]] = row_changed
    return


def coordinate_to_position(coordinate: str) -> tuple[int,int]:
    """
    Pre-conditions:
        Coordinate string must contain exactly two characters,
        The first letter should be an uppercase letter from 'A' to 'I'
        The second character should be a single digit character
        
    Convert the coordinate string entered into position on board

    Parameter:
        coordinate: Corresponding characters of certain position on board

    Returns:
        A tuple shows the (row,colomn) position on board
    """

    #store a mapping between first characters in coordinate string with there values
    dict_coordinate = {
        'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7,'I': 8
        }
        
    #get the tuple for return
    corresponded_position = ((int(coordinate[1])-1),
                             dict_coordinate.get(coordinate[0]))
    return corresponded_position


def can_place_ship(board: list[str], ship: list[tuple[int,int]]) -> bool:
    """
    Pre-conditions:
        All positions in ship must exit on board

    Check if the position is available to put a ship

    Parameter:
        board: Board used for game play
        ship: Positions of ship going to place

    Returns:
        True or False
    """

    #use for loop to determine every tuple in list 'ship'
    for position in ship:

        #if statement to determine whether square get is empty
        #if not empty, return 'False'
        if get_square(board,position) != '~':
                        return False
    #if empty, return 'True'
    return True


def place_ship(board: list[str], ship: list[tuple[int,int]]) -> None:
    """
    Pre-conditions:
        Ship should be able to be placed due to function can_place_ship

    Place ship if place available

    Parameter:
        board: Board used for game play
        ship: Positions of ship going to place

    Returns:
        None
    """

    #place a ship when can_place_ship returns 'True'
    if can_place_ship(board, ship) == True:
        for position in ship:
            change_square(board, position, ACTIVE_SHIP_SQUARE)
    return
              
                
def attack(board: list[str], position: tuple[int, int]) -> None:
    """
    Pre-conditions:
        Position must exit on board

    Determine whether the aim position met condition, if yes,
    change the charaacter to DEAD_SHIP_SQUARE,
    if not, change the character to MISS_SQUARE

    Parameters:
        board: Board used for game play
        position: Position used for determine

    Returns:
        None
    """

    #attack success if there is a placed ship
    if (get_square(board, position) == ACTIVE_SHIP_SQUARE or
        get_square(board, position) == DEAD_SHIP_SQUARE):
                change_square(board, position, DEAD_SHIP_SQUARE)

    #miss if there is no ship placed
    else:
        change_square(board, position, MISS_SQUARE)
    return


def display_board(board: list[str],show_ships: bool) -> None:
    """
    Pre-conditions:
        show_ships input should be 'True' or 'False'

    Show the board according to different show_ships value

    Parameter:
        board: Board used for game play
        show_ships: Bool value of whether the ships should be shown

    Returns:
        None
    """
        
    #get and print the board title
    row_length = len(board[0])
    title_string = HEADER_SEPARATOR + 'ABCDEFGHI'
    get_title = title_string[0:(row_length+2)]
    print(get_title)

    #print different board according to the value of show_ships
    for row_num,rows in enumerate(board,start = 1):
        if ACTIVE_SHIP_SQUARE in rows and show_ships == False:
            #replace ACTIVE_SHIP_SQUARE with EMPTY_SQUARE
            rows = rows.replace(ACTIVE_SHIP_SQUARE,EMPTY_SQUARE)
            print(row_num,ROW_SEPARATOR,rows, sep = "")
        else:
            print(row_num,ROW_SEPARATOR,rows, sep = "")
    return


def get_player_hp(board: list[str]) -> int:
    """
    Pre-conditions:
        null

    Show the player's hp (how many active ships)

    Parameter:
        board: Board used for game play

    Returns:
        An integer shows the number of active ships
    """

    #give initial value 0 to variable player_hp
    player_hp = 0
        
    #use loops to determine every character in 'board'
    for rows in board:
        for order in range(len(rows)):
            #count every ACTIVE_SHIP_SQUARE as
            #an addition of player_hp
            if rows[order] == ACTIVE_SHIP_SQUARE:
                player_hp = player_hp + 1
    return int(player_hp)


def display_game(p1_board: list[str], p2_board: list[str],
                 show_ships: bool) -> None:
    """
    Pre-coditions:
        null

    Show the player's whole game display

    Parameters:
        p1_board: Board used for player 1
        p2_board: Board used for player 2
        show_ships: Bool value of whether the ships should be shown

    Returns:
        None
    """

    #give initial values to variables
    life_p1 = 'life'
    life_p2 = 'life'
        
    #determine the player1's hp
    if get_player_hp(p1_board) != 1:
        
        life_p1 = 'lives'
    #determine the player2's hp
    if get_player_hp(p2_board) != 1:
        life_p2 = 'lives'
                
    #print player1's board
    print('PLAYER 1:', get_player_hp(p1_board), '{} remaining'.format(life_p1))
    display_board(p1_board, show_ships)
    #print player2's board
    print('PLAYER 2:', get_player_hp(p2_board), '{} remaining'.format(life_p2))
    display_board(p2_board, show_ships)
    return


def is_valid_coordinate(coordinate: str, board_size: int) -> tuple[bool,str]:
    """
    Pre-conditions:
        null

    Get different string corresponding to coordinate inputed

    Parameters:
        coordinate: A string contains the target position
        board_size: An integer shows the size of board

    Returns:
        Tuple contains relationship between elements inside
    """

    #determine different limits of coordinate string input
    #and get the corresponding output
    if len(coordinate) != 2:
        tuple_output = (False, INVALID_COORDINATE_LENGTH)        
    elif coordinate[0] not in 'ABCDEFGHI'[0:board_size]:
        tuple_output = (False, INVALID_COORDINATE_LETTER)       
    elif coordinate[1] not in '123456789'[0:board_size]:
        tuple_output = (False, INVALID_COORDINATE_NUMBER)     
    else:
        tuple_output = (True, '')
    return tuple_output


def is_valid_coordinate_sequence(coordinate_sequence: str, ship_length: int,
                                 board_size: int) -> tuple[bool, str]:
    """
    Pre-conditions:
        null

    Get different message string correspoding to coordinate_sequence input

    Parameters:
        coordinate_sequence: A string contains target positions of placing ship
        ship_length: An integer shows the length of ship going to place
        board_size: An integer shows the size of board

    Returns:
        Tuple contains relationship between elements inside
    """

    #split the sequence into separate strings(coordinates)
    coordinates = coordinate_sequence.split(',')
        
    #determine whether the length of input list correct
    if len(coordinates) != ship_length:
        tuple_output = (False, INVALID_COORDINATE_SEQUENCE_LENGTH)
    else:
        for coordinate in coordinates:
            
            #use is_valid_coordinate function to determine the coordinate input
            if is_valid_coordinate(coordinate, board_size)[0] == False:
                tuple_output = is_valid_coordinate(coordinate, board_size)
                return tuple_output
            else:
                tuple_output = (True,'')
                                
    return tuple_output
        

def build_ship(coordinate_sequence: str) -> list[tuple[int,int]]:
    """
    Pre-conditions:
        coordinate_sequence must represent a valid coordinate sequence

    Turns the coordinate_sequence into list of positions

    Parameters:
        coordinate_sequence: String shows coodinates input

    Returns:
        List of position tuples
    """

    #split coordinate_sequence into short coordinate strings
    coordinates = coordinate_sequence.split(',')
        
    #set an empty list for positions storing
    position_list = []
        
    #determine every coordinate in the list coordinates
    for coordinate in coordinates:
        #use coordinate_to_position function to convert
        #coordinate into position tuple
        position = coordinate_to_position(coordinate)
        position_list.append(position)
    return position_list



def setup_board(board_size: int, ship_sizes: list[int]) -> list[str]:
    """
    Pre-conditions:
        null

    Set a board for ship placing, ask for ship size and place ship for
    each ship size in asked position if position is valid

    Parameters:
        board_size: Integer shows value of n in 'n*n board' for game play
        ship_sizes: List of integers shows the size of ships to place

    Returns:
        List of stings shows the board after placing ships
    """
        
    #create an empty board
    board = create_empty_board(board_size)
        
    #judge every ship_size in list ship_sizes
    for ship_size in ship_sizes:
        
        #use an infinite while loop and onlly break when all tasks passed
        while True:
        
            #display the board first
            display_board(board, True)
                        
            #then asked for coordinates input
            coordinates = input('Enter a comma separated list of '
                                '{} coordinates: '.format(ship_size))
                        
            #use a if statement to determine whether
            #it's a valid coordinate sequence
            if (is_valid_coordinate_sequence(coordinates, ship_size,
                                             board_size)[0] == True):
            #convert coordinates input
            #into list of positions
                position_list = build_ship(coordinates)
                                
            #use another if statement to determine whether
            #the position asked can place a ship
                if can_place_ship(board, position_list) == True:
                    
                    #only place the ship and break the
                    #while loop after those two if
                    #statements got all True
                    place_ship(board, position_list)
                    break
                
                else:
                    
                    #print message for valid coordinate
                    #sequence but can't place ship
                    print(INVALID_SHIP_PLACEMENT)

            else:
                
                #print message for invalid coordinate sequence
                print(is_valid_coordinate_sequence(coordinates,
                                                   ship_size, board_size)[1])
    return board


def get_winner(p1_board: list[str], p2_board: list[str]) -> Optional[str]:
    """
    Pre-conditions：
        null

    Determine the hp for each player and return the corrsponding
    string shows the winner

    Parameters:
        p1_board: Game board for player 1
        p2_board: Game board for player 2

    Retruns:
        A string shows the winner
    """

    #get player's hp for each player
    player1_hp = get_player_hp(p1_board)
    player2_hp = get_player_hp(p2_board)
        
    #get the winner by determine the value of each player's hp left
    if player1_hp == 0:
        winner = 'PLAYER 2'
    elif player2_hp == 0:
        winner = 'PLAYER 1'
    else:
        winner = None
    return winner


def make_attack(target_board: list[str]) -> None:
    """
    Pre-coditions:
        null

    Ensure the input coordinate in target board is valid
    and use attack() function to get new values in board

    Parameters:
        target_board: Board used for game play

    Returns:
        None
    """

    #set an infinite while loop
    while True:
        #ask for the coordinate input
        coordinate = input(TURN_INPUT_MESSAGE)
                
        #determine whether the input coordinate is valid,
        #only break the loop and return
        #if the coordinate input is valid,
        #if not, print the corresponding message
        if is_valid_coordinate(coordinate, len(target_board))[0] == False:
            print(is_valid_coordinate(coordinate,
                                      len(target_board))[1])
        else:
            position = coordinate_to_position(coordinate)
            attack(target_board, position)
            return


if __name__ == "__main__":
    play_game()
