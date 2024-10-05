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

    def __init__(self) -> None:
        """
        Constructor for Weapon class.

        Parameters:
            symbol: The symbol of the weapon.
            name: The name of the weapon.
            effect: The effect of the weapon.
            range: The range of the weapon.
        """

        self._symbol = 'W'
        self._name = 'AbstractWeapon'
        self._effect = {}
        self._range = 0


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


        # Convert the Position into x, y coordinates of the weapon.
        x, y = position
        # Create an empty list to store the targets.
        targets = []

        #Use two for-loops to check all the positions in the weapon's range.
        #Only in a single direction.
        for dx in range(-self._range, self._range + 1):
            targets.append((x+dx, y))

        for dy in range(-self._range, self._range + 1):
            targets.append((x, y+dy))

        return targets

    def __str__(self) -> str:
        """
        Returns the name of the weapon.

        Return:
            A string of the name of the weapon.
        """
        return f"{self._name}"

    def __repr__(self) -> str:
        """
        Returns the instance which can be used to
        create a new identical weapon instance.

        Return:
            A string of the instance.
        """
        return f"{self.__class__.__name__}()"



class PoisonDart(Weapon):
    """
    A class to display details of the PoisonDart in the game.
    """

    def __init__(self) -> None:
        """
        Constructor for PoisonDart class.
        """

        # Use super() to call the __init__ method from the parent class.
        super().__init__()
        self._symbol = 'D'
        self._name = 'PoisonDart'
        self._effect = {'poison': 2}
        self._range = 2


class PoisonSword(Weapon):
    """
    A class to display details of the PoisonSword in the game.
    """

    def __init__(self) -> None:
        """
        Constructor for PoisonSword class.
        """

        # Use super() to call the __init__ method from the parent class.
        super().__init__()
        self._symbol = 'S'
        self._name = 'PoisonSword'
        self._effect = {'damage': 2, 'poison': 1}
        self._range = 1

class HealingRock(Weapon):
    """
    A class to display details of the HealingRock in the game.
    """

    def __init__(self) -> None:
        """
        Constructor for HealingRock class.
        """

        # Use super() to call the __init__ method from the parent class.
        super().__init__()
        self._symbol = 'H'
        self._name = 'HealingRock'
        self._effect = {'healing': 2}
        self._range = 2


class view():
    def __init__(self, ):
        pass


if __name__ == "__main__":
    main()
