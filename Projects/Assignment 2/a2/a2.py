import tkinter as tk
from tkinter import messagebox, filedialog
from typing import Callable, Optional

from support import *

# Implement the classes, methods & functions described in the task sheet here

def main():
    # Implement your main function here
    pass

class Weapon():
    """
    A class to display details of a weapon in the game.
    """

    def __init__(
            self,
            symbol: str,
            name: str,
            effect: dict[str, int],
            range: int
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
        return f"{self._name}"

    def get_symbol(self) -> str:
        """
        Returns the symbol of the weapon.

        Return:
            A string of the symbol of the weapon.
        """
        return f"{self._symbol}"

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
        pass

    def __str__(self) -> str:
        """
        Returns the name of the weapon.

        Return:
            A string of the name of the weapon.
        """
        return f"{self._name}"






class view():
    def __init__(self, ):
        pass


if __name__ == "__main__":
    main()
