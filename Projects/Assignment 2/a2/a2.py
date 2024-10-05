import tkinter as tk
from tkinter import messagebox, filedialog
from typing import Callable, Optional

from support import *

# Implement the classes, methods & functions described in the task sheet here

def main():
    # Implement your main function here
    pass

class Weapon:
    """
    A class to display details of a weapon in the game.
    """

    def __init__(
            self,
            symbol = 'W',
            name = 'AbstractWeapon',
            effect = {},
            range = 0
    ) -> None:
        """
        Constructor for Weapon class.

        Parameters:
            symbol: The symbol of the weapon.
            name: The name of the weapon.
            effect: The effect of the weapon.
            range: The range of the weapon.
        """

        self._symbol = symbol
        self._name = name
        self._effect = effect
        self._range = range


    def get_name(self) -> str:
        """
        Returns the name of the weapon.

        Return:
            A string of the name of the weapon.
        """
        return f'{self._name}'

    def get_symbol(self) -> str:
        """
        Returns the symbol of the weapon.

        Return:
            A string of the symbol of the weapon.
        """

        return f'{self._symbol}'

    def get_effect(self) -> dict[str, int]:
        """
        Returns the effect of the weapon.

        Return:
            A dictionary of the effect of the weapon.
        """
        return self._effect

    def get_targets(self, position: Position) -> list[Position]:
        """
        Returns the list of all positions within the range for this weapon.

        Parameters:
            position: The position which the weapon currently at.

        Return:
            A list of positions in range.
        """

        # Convert the Position into x, y coordinates of the weapon.
        x, y = position
        # Create an empty list to store the targets.
        targets = []

        #Use two for-loops to check all the positions in the weapon's range.
        for dx in range(-self._range, self._range + 1):
            for dy in range(-self._range, self._range + 1):
                #Use an if-statement to check if the
                #manhattan distance is in the weapon's range,
                #if so, append the position to the targets list.
                if abs(dx) + abs(dy) <= self._range:
                    targets.append((x + dx, y + dy))

        return targets

    def __str__(self) -> str:
        """
        Returns the name of the weapon.

        Return:
            A string of the name of the weapon.
        """
        return f'{self._name}'

    def __repr__(self) -> str:
        """
        Returns the instance which can be used to
        create a new identical weapon instance.

        Return:
            A string of the instance.
        """
        return (f'Weapon({self._symbol}, '
                f'{self._name}, '
                f'{self._effect}, '
                f'{self._range})'
                )

class PoisonDart(Weapon):
    """
    A class to display details of a Poison Dart weapon in the game.
    """

    def __init__(self) -> None:
        """
        Constructor for PoisonDart class.
        """

        # Use super() to call the __init__ method from the parent class.
        super().__init__('D', 'Poison Dart', {'poison': 2}, 2)





class view():
    def __init__(self, ):
        pass


if __name__ == "__main__":
    main()
