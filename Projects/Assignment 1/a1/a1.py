from typing import Optional
from support import *


def play_game() -> None:
        pass


def num_hour() -> float:
        return


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
        board_rows = '~' * board_size
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
        row_changed = row_get[0:position[1]] + new_square + row_get[(position[1]+1):]
        #put the changed row back into the board
        board[position[0]] = row_changed
        return


def coordinate_to_position(coordinate: str) -> tuple[int,int]:
        """
        Pre-conditions:
                coordinate string must contain exactly two characters,
                the first letter should be an uppercase letter from 'A' to 'I'
                the second character should be a single digit character
        
        Convert the coordinate string entered into position on board

        Parameter:
                coordinate: Corresponding characters of certain position on board

        Returns:
                A tuple shows the (row,colomn) position on board
        """

        #store a mapping between first characters in coordinate string with there values
        dict_coordinate = {'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7,'I': 8}
        #get the tuple for return
        corresponded_position = ((int(coordinate[1])-1),dict_coordinate.get(coordinate[0]))
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
                row_num = position[0]
                colomn_num = position[1]
        #determine whether this position is empty, if empty, return 'True'
                if board[row_num][colomn_num] == '~':
                        return True
                else:
                        return False


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

        if can_place_ship(board, ship) == True:
                for position in ship:
                        row_place = position[0]
                        colomn_place = position[1]
                        board[row_place] = (board[row_place][0:colomn_place]
                        + 'O' + board[row_place][colomn_place+1:])
        return
              
                
def attack(board: list[str], position: tuple[int, int]) -> None:
        """
        Pre-conditions:
                Position must exit on board

        Determine whether the aim position met condition, if yes,
        change the charaacter to 'X', if not, change the character to '!'

        Parameter:
                board: Board used for game play
                position: Position used for determine

        Returns:
                None
        """
        
        row_attack = position[0]
        colomn_attack = position[1]
        if board[row_attack][colomn_attack] == 'O':
                board[row_attack] = (board[row_attack][0:colomn_attack]
                + 'X' + board[row_attack][colomn_attack+1:])       
        elif board[row_attack][colomn_attack] == 'X':
                board[row_attack] = (board[row_attack][0:colomn_attack]
                + 'X' + board[row_attack][colomn_attack+1:])
        else:
                board[row_attack] = (board[row_attack][0:colomn_attack]
                + '!' + board[row_attack][colomn_attack+1:])
        return






#board_size = int(input('Enter board size:'))
#board = create_empty_board(board_size)




if __name__ == "__main__":
    play_game()
