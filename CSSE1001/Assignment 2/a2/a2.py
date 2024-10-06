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
    A subclass to display details of the PoisonDart in the game.
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
    A subclass to display details of the PoisonSword in the game.
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
    A subclass to display details of the HealingRock in the game.
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



class Slug(Entity):
    """
    A subclass to display the details of the slugs in the game.
    """

    def __init__(self, max_health: int) -> None:
        """
        Constructor for Slug subclass.
        """

        # Use super() to call the __init__ method from the Entity class.
        super().__init__(max_health)
        self._symbol = SLUG_SYMBOL
        self._can_move = True #assuming the slug can move.


    def choose_move(self,
                    candidates: list[Position],
                    current_position: Position,
                    player_position: Position
                    ) -> Position:
        """
        Returns the next position of the slug.
        (Need to be implemented in the subclasses)
        """

        #Raise an error if this method is not override with
        #a valid implementation in the subclasses.
        raise NotImplementedError(
            'Slug subclasses must implement a choose_move method.'
        )


    def can_move(self) -> bool:
        """
        Returns True if the slug can move on this turn, otherwise False.

        Return:
            A boolean value shows if the slug can move.
        """

        return self._can_move


    def end_turn(self) -> None:
        """
        Registers the slug has completed its turn.
        """

        #Use if statement to judge if the slug can move,
        #if so, set the value of can_move to False,
        #Otherwise, set the value of can_move to True.
        if self._can_move:
            self._can_move = False
        else:
            self._can_move = True



class NiceSlug(Slug):
    """
    A subclass to display the details of the NiceSlug in the game.
    """

    def __init__(self) -> None:
        """
        Constructor for NiceSlug subclass.
        """

        #Use super() to call the __init__ method from the Slug subclass.
        super().__init__(max_health=10)
        #The default weapon of the NiceSlug is HealingRock.
        self._weapon = HealingRock()
        self._symbol = NICE_SLUG_SYMBOL


    def choose_move(self,
                    candidates: list[Position],
                    current_position: Position,
                    player_position: Position
                    ) -> Position:
        """
        Returns the next position of this slug.
        """

        #The NiceSlug always stays in the same position.
        return current_position


    def __repr__(self) -> str:
        """
        Returns the instance which can be used to
        create a new identical NiceSlug instance.

        Return:
            A string of the instance.
        """

        return f"{self.__class__.__name__}()"



#Define a function to calculate the Euclidean distance between two positions.
def euclidean_distance(position1: Position, position2: Position) -> float:
    """
    Returns the Euclidean distance between two positions.

    Parameters:
        position1: The first position.
        position2: The second position.

    Return:
        A float of the Euclidean distance between two positions.
    """

    #Calculate the Euclidean distance between two positions.
    return (
            ((position1[0] - position2[0])**2 +
            (position1[1] - position2[1])**2)**0.5
    )



class AngrySlug(Slug):
    """
    A subclass to display the details of the AngrySlug in the game.
    """

    def __init__(self) -> None:
        """
        Constructor for AngrySlug subclass.
        """

        #Use super() to call the __init__ method from the Slug subclass.
        super().__init__(max_health=5)
        #The default weapon of the AngrySlug is PoisonSword.
        self._weapon = PoisonSword()
        self._symbol = ANGRY_SLUG_SYMBOL


    def choose_move(self,
                    candidates: list[Position],
                    current_position: Position,
                    player_position: Position
                    ) -> Position:
        """
        Returns the next position of this slug.
        """

        #Set the default target position as the current position.
        target_position = current_position

        #Use for-loop to judge all the positions in the candidates list.
        for position in candidates:
            #If the Euclidean distance between this position
            #and the player_position is smaller than the distance between
            #the target_position and the player_position,
            #set the target_position as this position.
            if (
                euclidean_distance(position, player_position) <
                euclidean_distance(target_position, player_position)
            ):
                target_position = position
            #If the Euclidean distance between this position
            #and the player_position is equal to the distance between
            #the target_position and the player_position,
            #set the target_position as the smaller tuple.
            elif (
                euclidean_distance(position, player_position) ==
                euclidean_distance(target_position, player_position)
            ):
                if position < target_position:
                    target_position = position

        return target_position


    def __repr__(self) -> str:
        """
        Returns the instance which can be used to
        create a new identical NiceSlug instance.

        Return:
            A string of the instance.
        """

        return f"{self.__class__.__name__}()"



class ScaredSlug(Slug):
    """
    A subclass to display the details of the ScaredSlug in the game.
    """

    def __init__(self) -> None:
        """
        Constructor for ScaredSlug subclass.
        """

        #Use super() to call the __init__ method from the Slug subclass.
        super().__init__(max_health=3)
        #The default weapon of the ScaredSlug is PoisonDart.
        self._weapon = PoisonDart()
        self._symbol = SCARED_SLUG_SYMBOL


    def choose_move(self,
                    candidates: list[Position],
                    current_position: Position,
                    player_position: Position
                    ) -> Position:
        """
        Returns the next position of this slug.
        """

        #Set the default target position as the current position.
        target_position = current_position

        #Use for-loop to judge all the positions in the candidates list.
        for position in candidates:
            #If the Euclidean distance between this position
            #and the player_position is larger than the distance between
            #the target_position and the player_position,
            #set the target_position as this position.
            if (
                euclidean_distance(position, player_position) >
                euclidean_distance(target_position, player_position)
            ):
                target_position = position
            #If the Euclidean distance between this position
            #and the player_position is equal to the distance between
            #the target_position and the player_position,
            #set the target_position as the larger tuple.
            elif (
                euclidean_distance(position, player_position) ==
                euclidean_distance(target_position, player_position)
            ):
                if position > target_position:
                    target_position = position

        return target_position


    def __repr__(self) -> str:
        """
        Returns the instance which can be used to
        create a new identical NiceSlug instance.

        Return:
            A string of the instance.
        """

        return f"{self.__class__.__name__}()"



class SlugDungeonModel:
    """
    A class to model the logic of the game.
    """

    def __init__(self, tiles: list[list[Tile]], slugs: dict[Position, Slug],
                 player: Player, player_position: Position) -> None:
        """
        Constructor for SlugDungeonModel class.
        """

        self._tiles = tiles
        self._slugs = slugs
        self._player = player
        self._player_position = player_position


    def get_tiles(self) -> list[list[Tile]]:
        """
        Returns the tiles of the game.

        Return:
            A list of list of Tile instances.
        """

        return self._tiles


    def get_slugs(self) -> dict[Position, Slug]:
        """
        Returns the slugs in the game.

        Return:
            A dictionary of slug positions and Slug instances.
        """

        return self._slugs


    def get_player(self) -> Player:
        """
        Returns the player in the game.

        Return:
            A Player instance.
        """

        return self._player


    def get_player_position(self) -> Position:
        """
        Returns the current position of the player.

        Return:
            A tuple of the position of the player.
        """

        return self._player_position


    def get_tile(self, position: Position) -> Tile:
        """
        Returns the tile at the given position.

        Parameters:
            position: The position of the tile.

        Return:
            A Tile instance.
        """

        return self._tiles[position[0]][position[1]]


    def get_dimensions(self) -> tuple[int, int]:
        """
        Returns the dimensions of the dungeon.

        Return:
            A tuple of the dimensions of the dungeon.
        """

        return len(self._tiles), len(self._tiles[0])


    def get_valid_slug_positions(self, slug: Slug) -> list[Position]:
        """
        Pre-condition:
            slug is ine of the alive slugs in the game.

        Returns the valid positions for the slug to move to.

        Parameters:
            slug: The Slug instance.

        Return:
            A list of valid positions.
        """

        #Set an empty list to store the valid next positions.
        valid_positions = []

        #Use if statement to judge if the input slug can move.
        if slug.can_move():
            #Get the current position of the input slug.
            for slug_position, slug_type in self._slugs.items():
                #Use if statement to judge if the input slug is the same
                #type of slug as in the dictionary of slugs, if so, append
                #the corresponding position into the valid_positions list.
                if slug == slug_type:
                    current_position = slug_position
                    #Append the current position into the valid_positions list.
                    valid_positions.append(current_position)

                    #Set the available movements of the slug.
                    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                    for dx, dy in movements:
                        #Get the possible next positions of the slug.
                        next_position = (
                            current_position[0] + dx,
                            current_position[1] + dy
                        )

                        #Use if statement to judge if
                        #the next position is inside the dungeon.
                        if (
                            0 <= next_position[0] < len(self._tiles) and
                            0 <= next_position[1] < len(self._tiles[0])
                        ):
                            #Use if statement to judge if the next position
                            #is not blocking and not occupied by other slugs,
                            #and not occupied by the player.
                            if (
                                not self.get_tile(next_position).is_blocking()
                                and next_position not in self._slugs.keys()
                                and next_position is not self._player_position
                            ):
                                #Append the next position into
                                #the valid_positions list.
                                valid_positions.append(next_position)

        return valid_positions





class view():
    def __init__(self, ):
        pass


if __name__ == "__main__":
    main()
