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
        
        Get the position on board by entering a coordinate string

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






#board_size = int(input('Enter board size:'))
#board = create_empty_board(board_size)




if __name__ == "__main__":
    play_game()
