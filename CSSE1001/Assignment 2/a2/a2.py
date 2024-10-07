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


    def get_symbol(self) -> str:
        """
        Returns the symbol of the tile.

        Return:
            A string of the symbol of the tile.
        """

        return self._symbol


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
            slug is in of the alive slugs in the game.

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


    def perform_attack(self, entity: Entity, position: Position) -> None:
        """
        Performs an attack by the input entity at the input position.

        Parameters:
            entity: The Entity instance.
            position: The position of this entity.
        """

        #Get the weapon hold by this entity.
        weapon = entity.get_weapon()

        #Use if statement to judge if the entity has a weapon.
        if weapon is not None:
            #Get the available targets in the weapon's range.
            targets = weapon.get_targets(position)

            #Use for loop to judge all the targets in the targets list.
            for target in targets:

                #Use if statement to make sure the target position is
                #inside the dungeon.
                if (
                    0 <= target[0] < len(self._tiles) and
                    0 <= target[1] < len(self._tiles[0])
                ):
                    #Use if statement to judge if the target position
                    #is occupied by a slug and the attacker is the player.
                    if (
                        target in self._slugs.keys() and
                        isinstance(entity, Player)
                    ):
                        #Get the slug in the target position.
                        slug = self._slugs[target]
                        #Get the effect of the weapon.
                        effects = weapon.get_effect()
                        #Apply the effect to the slug.
                        slug.apply_effects(effects)
                    #Use if statement to judge if the target position
                    #is occupied by the player and the attacker is a slug.
                    elif(
                        target == self._player_position and
                        isinstance(entity, Slug)
                    ):
                        #Get the effect of the weapon.
                        effects = weapon.get_effect()
                        #Apply the effects to the player.
                        self._player.apply_effects(effects)


    def end_turn(self) -> None:
        """
        Handles the steps should occur after the player moved.
        """

        #Apply the player's poison.
        self._player.apply_poison()

        #Set a new dictionary for storing alive slugs.
        alive_slugs = {}

        #Use for loop to judge all the slugs in the slugs dictionary.
        for slug_position, slug in self._slugs.items():
            #Apply the poison to the slugs.
            slug.apply_poison()
            #Use if statement to judge if the slug is alive
            #after applying poison.
            if not slug.is_alive():
                #Set the tile to have the weapon of the dead slug if any.
                Tile.set_weapon(
                    self.get_tile(slug_position),
                    slug.get_weapon()
                )

            else:
                #Append the alive slug into the alive_slugs dictionary.
                alive_slugs[slug_position] = slug

        #Set a new dictionary for storing the slugs after moving.
        moved_slugs = {}
        #Use for loop to let all alive slugs to move and attack.
        for slug_position, slug in alive_slugs.items():
            #Use if statement to judge if the slug can move.
            if slug.can_move():
                new_slug_position = slug.choose_move(
                    self.get_valid_slug_positions(slug),
                    slug_position,
                    self._player_position
                )

                moved_slugs[new_slug_position] = slug
                #Slug attacks
                self.perform_attack(slug, new_slug_position)

            else:
                moved_slugs[slug_position] = slug

            #State the slug has completed its turn,
            #used for toggle the can_move status.
            slug.end_turn()

        #Update the slugs dictionary.
        self._slugs = moved_slugs


    def handle_player_move(self, position_delta: Position) -> None:
        """
        Handles the player's move.
        """

        #Get the possible new position of the player.
        player_new_position = (
            self._player_position[0] + position_delta[0],
            self._player_position[1] + position_delta[1]
        )


        #Use if statement to judge if the new position is inside the dungeon.
        if (
            0 <= player_new_position[0] < len(self._tiles) and
            0 <= player_new_position[1] < len(self._tiles[0])
        ):
            #Use if statement to judge if the new position is not blocking.
            if not self.get_tile(player_new_position).is_blocking():
                #Update the player's position.
                self._player_position = player_new_position
                #Use if statement to judge if there is a weapon on the tile.
                if Tile.get_weapon(
                        self.get_tile(self._player_position)
                ) is not None:
                    #Equip the weapon on the tile to the player.
                    self._player.equip(
                        Tile.get_weapon(self.get_tile(self._player_position))
                    )
                    #Remove the weapon from the tile.
                    Tile.remove_weapon(self.get_tile(self._player_position))

                self.perform_attack(self._player, self._player_position)
                self.end_turn()


    def has_won(self) -> bool:
        """
        Returns True if the player has won, otherwise False.

        Return:
            A boolean value of the game state.
        """

        #Get the tile which the player is on.
        player_tile = self.get_tile(self._player_position)
        #Determine if the player is on the goal tile and all slugs dead,
        #if so, return True, otherwise, return False.
        return (
            player_tile.get_symbol() == GOAL_TILE
            and
            self._slugs == {}
        )


    def has_lost(self) -> bool:
        """
        Returns True if the player has lost, otherwise False.

        Return:
            A boolean value of the game state.
        """

        #Determine if the player is dead, if so, return True,
        #otherwise, return False.
        return not self._player.is_alive()



def load_level(filename: str) -> SlugDungeonModel:
    """
    Read the level from the file and return a SlugDungeonModel instance.

    Parameters:
        filename: The name of the file to read.
    """

    #Open the file with the input filename.
    with open(filename, 'r') as level_file:
        #Read the content of the file.
        content = level_file.readlines()
        #Get the player's max_health from the first line of the content.
        player_max_health = int(content[0])
        #Set the default values for the variables used for
        #SlugDungronModel initializer.
        read_tiles = []
        read_slugs = {}
        read_player = None
        player_position = ()

        #Use for loop to judge all the lines in the content list.
        for row_order, line in enumerate(content[1:], start=0):
            #Create an empty list to store the rows.
            rows = []
            #Use for loop to judge all the characters in the line.
            for column_order, char in enumerate(line[:-1], start=0):
                #Use if statement to judge the character in the line and
                #create the corresponding tile instance.
                if char == WALL_TILE:
                    rows.append(create_tile(WALL_TILE))
                elif char == GOAL_TILE:
                    rows.append(create_tile(GOAL_TILE))
                elif char == PLAYER_SYMBOL:
                    read_player = Player(player_max_health)
                    player_position = (row_order, column_order)
                    rows.append(create_tile(FLOOR_TILE))
                elif char == NICE_SLUG_SYMBOL:
                    read_slugs[(row_order, column_order)] = NiceSlug()
                    rows.append(create_tile(FLOOR_TILE))
                elif char == ANGRY_SLUG_SYMBOL:
                    read_slugs[(row_order, column_order)] = AngrySlug()
                    rows.append(create_tile(FLOOR_TILE))
                elif char == SCARED_SLUG_SYMBOL:
                    read_slugs[(row_order, column_order)] = ScaredSlug()
                    rows.append(create_tile(FLOOR_TILE))
                else:
                    rows.append(create_tile(char))
            #Append the rows into the tiles list.
            read_tiles.append(rows)

        #Create a new SlugDungeonModel instance with the read values.
        return SlugDungeonModel(read_tiles, read_slugs, read_player, player_position)











class view():
    def __init__(self, ):
        pass


if __name__ == "__main__":
    main()
    file = load_level("./levels/leveltest.txt")
    file._player = Player(25)
    file._slugs = {
        (1, 3): ScaredSlug(),
        (2, 1): NiceSlug(),
        (2, 2): AngrySlug(),
        (2, 4): ScaredSlug(),
        (4, 2): AngrySlug(),
    }
    # Convert level string to proper tiles


    slugs = {
        (1, 3): ScaredSlug(),
        (2, 1): NiceSlug(),
        (2, 2): AngrySlug(),
        (2, 4): ScaredSlug(),
        (4, 2): AngrySlug(),
    }
    player = Player(25)

    model = SlugDungeonModel(
        file._tiles, slugs, player, (1, 1)
    )

    # Setup sword to player right
    sword = PoisonSword()
    tile_to_right = model.get_tile((1, 2))
    tile_to_right.set_weapon(sword)
    print(player.get_health())
    # Player moves right
    player.apply_effects({"poison": 1, "damage": 5})
    print(player.get_health())
    model.handle_player_move((0, 1))
    #assertNotEqual(model.get_slugs(), slugs)
    print(player.get_health())
    print(player.get_health() == 25 - 5 - 2 - 1)

    # # Assert that player damaged the enemies
    # len(model.get_slugs()) == 4
    # angry_slug_position = (2, 2)
    # angry_slug = model.get_slugs().get(angry_slug_position)
    # angry_slug.get_health() == 2





