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
        while order_colomns < board_size:
                board.append([board_rows])
                order_colomns += 1
        return board

def get_square(board: list[str], position: tuple[int,int]) ->str:
        """
        Pre-conditions:
                position must exist on board

        get the thing shows in board in a specific position

        Parameter:
                board: Board used for searching things
                position: Position of things to be searched

        Returns:
                A string shows the thing find in that position
        """

        

if __name__ == "__main__":
    play_game()
