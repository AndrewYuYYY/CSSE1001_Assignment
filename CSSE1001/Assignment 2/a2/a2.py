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

        #Set a default value for the Weapon class variables.
        self._symbol = WEAPON_SYMBOL
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

        #Use two for-loops to judge all the positions in the weapon's range.
        #Only in a single direction.
        for dx in range(-self._range, self._range + 1):
            # If statements used to exclude the current position.
            if dx == 0:
                continue
            else:
                targets.append((x+dx, y))
        #Judge for y direction.
        for dy in range(-self._range, self._range + 1):
            if dy == 0:
                continue
            else:
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
        self._symbol = POISON_DART_SYMBOL
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
        self._symbol = POISON_SWORD_SYMBOL
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
        self._symbol = HEALING_ROCK_SYMBOL
        self._name = 'HealingRock'
        self._effect = {'healing': 2}
        self._range = 2



class Tile:
    """
    A class to display individual positions in the dungeon.
    """

    def __init__(self, symbol: str, is_blocking: bool) -> None:
        """
        Constructor for Tile class.

        Parameters:
            symbol: The symbol of the tile.
            is_blocking: A boolean value to show if the tile is blocking.
        """

        self._symbol = symbol
        self._is_blocking = is_blocking
        #Set the default value of the weapon as None.
        self._weapon = None


    def is_blocking(self) -> bool:
        """
        Returns the status of the tile.

        Return:
            A boolean value to show if the tile is blocking.
        """

        return self._is_blocking


    def get_weapon(self) -> Optional[Weapon]:
        """
        Returns the weapon on the tile if there is one, otherwise None.

        Return:
            A Weapon object shows the weapon on the tile or None.
        """

        return self._weapon


    def set_weapon(self, weapon: Weapon) ->None:
        """
        Sets the weapon on the current tile.

        Parameters:
            weapon: The weapon need to be set on the tile.
        """

        #Reset the value of the weapon to be the input weapon.
        self._weapon = weapon


    def remove_weapon(self) -> None:
        """
        Removes the weapon on the current tile.
        """

        self._symbol = FLOOR_TILE


    def __str__(self) -> str:
        """
        Returns the symbol of the tile.

        Return:
            A string of the symbol of the tile.
        """

        return f"{self._symbol}"


    def __repr__(self) -> str:
        """
        Returns the instance which can be used to
        create a new identical tile instance.

        Return:
            A string of the instance.
        """

        return f"{self.__class__.__name__}('{self._symbol}', {self._is_blocking})"



def create_tile(symbol: str) -> Tile:
    """
    Pre-condition:
    symbol is a string.

    Returns a new Tile instance based on the symbol.

    Parameters:
        symbol: A string shows the symbol of the tile.

    Return:
        A new Tile instance.
    """

    #Create a default new tile instance with
    #symbol of FLOOR_TILE and is_blocking as False.
    new_tile = Tile(FLOOR_TILE, False)

    #Use if-elif statements to judge the symbol input,
    #if the symbol is not one of the weapon symbols, return the tile instance.
    #Otherwise, set the weapon on the tile and return the tile instance.
    if symbol == WALL_TILE:
        return Tile(symbol, True)
    elif symbol == GOAL_TILE:
        return Tile(symbol, False)
    elif symbol == POISON_DART_SYMBOL:
        new_tile.set_weapon(PoisonDart())
    elif symbol == POISON_SWORD_SYMBOL:
        new_tile.set_weapon(PoisonSword())
    elif symbol == HEALING_ROCK_SYMBOL:
        new_tile.set_weapon(HealingRock())
    return new_tile



class Entity:
    """
    A class to display the details of entities in the game.
    """

    def __init__(self, max_health: int) -> None:
        """
        Constructor for Entity class.

        Parameters:
            max_health: A integer shows the maximum health of the entity.
        """

        #Set the default value of the Entity class variables.
        self._max_health = max_health #used for reset health
        self._health = max_health
        self._poison = 0
        self._weapon = None
        self._symbol = ENTITY_SYMBOL

    def get_symbol(self) -> str:
        """
        Returns the symbol of the entity.

        Return:
            A string of the symbol of the entity.
        """

        return self._symbol


    def get_name(self) -> str:
        """
        Returns the name of the entity.

        Return:
            A string of the name of the entity.
        """

        return f"{self.__class__.__name__}"


    def get_health(self) -> int:
        """
        Returns the current health of the entity.

        Return:
            An integer of the current health of the entity.
        """

        return self._health


    def get_poison(self) -> int:
        """
        Returns the current poison state of the entity.

        Return:
            An integer of the current poison state of the entity.
        """

        return self._poison


    def get_weapon(self) -> Optional[Weapon]:
        """
        Returns the weapon of the entity.

        Return:
            A Weapon object shows the weapon hold be the entity or None.
        """

        return self._weapon


    def equip(self, weapon: Weapon) -> None:
        """
        Equips the weapon to the entity.

        Parameters:
            weapon: The weapon object need to be equipped to the entity.
        """

        #Set the weapon of the entity to be the input weapon.
        self._weapon = weapon


    def get_weapon_targets(self, position: Position) -> list[Position]:
        """
        Returns the list of all positions this entity
        can attack with the weapon.

        Parameters:
            position: The position which the entity currently at.

        Return:
            A list of positions in attack range,
            if no weapon, return an empty list.
        """

        #If the entity does not hold a weapon, return an empty list.
        if self._weapon is None:
            return []

        #Otherwise, return the available targets of the weapon.
        return self._weapon.get_targets(position)


    def get_weapon_effect(self) -> dict[str, int]:
        """
        Returns the effect of the weapon hold by the entity.

        Return:
            A dictionary of the effects of the weapon.
        """

        #If the entity does not hold a weapon, return an empty dictionary.
        if self._weapon is None:
            return {}

        #Otherwise, return the effects of the weapon.
        return self._weapon.get_effect()


    def apply_effects(self, effects: dict[str, int]) -> None:
        """
        Applies the effects to the entity.

        Parameters:
            effects: A dictionary of the effects active weapon had.
        """

        #Use for-loop to repeat looking all the effects
        #in the input effects dictionary.
        for effect, amount in effects.items():
            #Use if statement to judge the effect type
            #and apply the amount of corresponding effect.
            if effect == 'damage':
                self._health -= amount
                #Use if statement to judge if the health is below 0,
                #if so, set the health to 0.
                if self._health < 0:
                    self._health = 0
            elif effect == 'healing':
                self._health += amount
                #Use if statement to judge if the health is above
                #the max health, if so, set the health to the max health.
                if self._health > self._max_health:
                    self._health = self._max_health
            elif effect == 'poison':
                self._poison += amount


    def apply_poison(self) -> None:
        """
        Applies the amount of poison effect to the entity.
        """

        #Use if statement to judge if the poison effect will be applied.
        if self._health > 0 and self._poison > 0:
            #Reduce the health of entity by the amount of poison state.
            self._health -= self._poison
            # Use if statement to judge if the health is below 0,
            # if so, set the health to 0.
            if self._health < 0:
                self._health = 0
            #Reduce the poison state by 1.
            self._poison -= 1


    def is_alive(self) -> bool:
        """
        Returns True if the entity is alive, otherwise False.

        Return:
            A boolean value shows if the entity is alive.
        """

        return self._health > 0


    def __str__(self) -> str:
        """
        Returns the name of the entity.

        Return:
            A string of the name of the entity.
        """

        return f"{self.__class__.__name__}"


    def __repr__(self) -> str:
        """
        Returns the instance which can be used to
        create a new identical entity instance.

        Return:
            A string of the instance.
        """

        return f"{self.__class__.__name__}({self._max_health})"


class Player(Entity):
    """
    A class to display the details of the player in the game.
    """

    def __init__(self, max_health: int) -> None:
        """
        Constructor for Player class.
        """

        # Use super() to call the __init__ method from the Entity class.
        super().__init__(max_health)
        self._symbol = PLAYER_SYMBOL





class view():
    def __init__(self, ):
        pass


if __name__ == "__main__":
    main()
