import tkinter as tk
from doctest import master
from fileinput import filename
from tkinter import messagebox, filedialog
from typing import Callable, Optional

from support import *




def main() -> None:
    """
    Handle the game play.
    """
    root = tk.Tk()
    play_game(root, './levels/level1.txt')


class Weapon:
    """
    A class to display details of a weapon in the game.
    """

    def __init__(self) -> None:
        """
        Constructor for Weapon class.
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
        self._weapon = None


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

        return (
            f"{self.__class__.__name__}"
            f"('{self._symbol}', {self._is_blocking})"
        )



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
        # print("before apply_effects")
        # print(Player.get_health(self))
        # print("====================")
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
        # print("after apply_effects")
        # print(Player.get_health(self))
        # print("====================")


    def apply_poison(self) -> None:
        """
        Applies the amount of poison effect to the entity.
        """
        # print("before apply_poison")
        # print(Player.get_health(self))
        # print("====================")
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

        # print("after apply_poison")
        # print(Player.get_health(self))
        # print("====================")




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
        self._slugs = slugs.copy()
        self._player = player
        self._player_position = player_position
        self._player_previous_position = player_position


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
                        #the next position is inside the dungeon and
                        #not blocking and not occupied by slugs and
                        #not the same as the player's position.
                        if (
                            0 <= next_position[0] < len(self._tiles) and
                            0 <= next_position[1] < len(self._tiles[0]) and
                            not self.get_tile(next_position).is_blocking() and
                            next_position not in self._slugs.keys() and
                            next_position != self._player_position
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
                #Add the alive slug into the alive_slugs dictionary.
                alive_slugs[slug_position] = slug

        #Updated the slugs dictionary to the alive slugs.
        self._slugs = alive_slugs
        #Get a copy of the Slugs dictionary.
        slugs_copy = self._slugs.copy()
        #Use for loop to let all alive slugs to move.
        for slug_position, slug in slugs_copy.items():
            #Use if statement to judge if the slug can move.
            if slug.can_move():
                #print('test', self.get_valid_slug_positions(slug))
                new_slug_position = slug.choose_move(
                    self.get_valid_slug_positions(slug),
                    slug_position,
                    self._player_previous_position
                )

                del self._slugs[slug_position]
                self._slugs[new_slug_position] = slug

        #Use for loop to let all alive slugs to attack.
        for slug_position, slug in self._slugs.items():
            self.perform_attack(slug, slug_position)
            # State the slug has completed its turn,
            # used for toggle the can_move status.
            slug.end_turn()


    def handle_player_move(self, position_delta: Position) -> None:
        """
        Handles the player's move.
        """

        #Get the possible new position of the player.
        player_new_position = (
            self._player_position[0] + position_delta[0],
            self._player_position[1] + position_delta[1]
        )

        #Use if statement to judge if the new position is inside the dungeon
        #and not blocking and not occupied by slugs.
        if (
            0 <= player_new_position[0] < len(self._tiles) and
            0 <= player_new_position[1] < len(self._tiles[0]) and
            not self.get_tile(player_new_position).is_blocking() and
            player_new_position not in self._slugs.keys()
        ):
            #Store the previous position and update the new position.
            self._player_previous_position = self._player_position
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

            #Plsyer perform attack.
            self.perform_attack(self._player, self._player_position)
            #End the player's turn and slugs move and attack.
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
        for row_order, line in enumerate(content[1:]):
            #Create an empty list to store the rows.
            rows = []
            #Use for loop to judge all the characters in the line.
            for column_order, char in enumerate(line[:-1]):
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



def play_game(root: tk.Tk, file_path: str) -> None:
    """
    Constructs the controller instance using the root and the given file_path.

    Parameters:
        root: The Tk instance.
        file_path: The file path of the level files.
    """

    SlugDungeon(root, file_path)
    root.mainloop()



class DungeonMap(AbstractGrid): #One class in view
    def __init__(self,
        master: Union[tk.Tk, tk.Frame],
        dimensions: tuple[int, int],
        size: tuple[int, int],
        **kwargs,
    ) -> None:
        """
        Constructor for the DungeonMap class.

        Parameters:
            master: The master widget.
            dimensions: A tuple of the rows and columns of the dungeon.
            size: A tuple of the size of the dungeon in pixel.
        """
        super().__init__(master, dimensions, size, **kwargs)


    def redraw(self, tiles: list[list[Tile]], player_position: Position,
               slugs: dict[Position, Slug]) -> None:
        """
        Redraws the dungeon map.

        Parameters:
            tiles: A list of list of Tile instances.
            player_position: A tuple of the player's position.
            slugs: A dictionary of the slug positions and the Slug instances.
        """

        self.clear()
        for row_order, tile_row in enumerate(tiles):
            for column_order, tile in enumerate(tile_row):
                tile_symbol = tile.get_symbol()
                weapon_on_tile = tile.get_weapon()

                #Get the position, bounding box of the tile.
                position = (row_order, column_order)
                bounding_box = self.get_bbox(position)

                #Use an extremely long if statements to draw the tiles
                #with different symbols input.
                if tile_symbol == WALL_TILE:
                    self.create_rectangle(bounding_box, fill=WALL_COLOUR)
                elif tile_symbol == FLOOR_TILE:
                    self.create_rectangle(bounding_box, fill=FLOOR_COLOUR)
                    #Use if statement to judge if there is a weapon on the tile
                    #if so, give the weapon's notation on the tile.
                    if weapon_on_tile is not None:
                        self.annotate_position(position, weapon_on_tile.get_symbol())

                elif tile_symbol == GOAL_TILE:
                    self.create_rectangle(bounding_box, fill=GOAL_COLOUR)


        #Get the bounding_box of the player.
        bounding_box_player = self.get_bbox(player_position)
        #Draw and add the notation of the player on the map.
        self.create_oval(bounding_box_player, fill=PLAYER_COLOUR)
        self.annotate_position(player_position, 'Player')


        #Use for loop to judge all the slugs in the slugs dictionary.
        for slug_position, slug in slugs.items():
            #Get the bounding_box of the slug.
            bounding_box_slug = self.get_bbox(slug_position)

            #Draw the slug on the map.
            self.create_oval(bounding_box_slug, fill=SLUG_COLOUR)

            #Use if statement to judge the type of the slug.
            if isinstance(slug, NiceSlug):
                #Put the notation of slug type to be 'NiceSlug'.
                self.annotate_position(slug_position, 'Nice\nSlug')
            elif isinstance(slug, AngrySlug):
                #Put the notation of slug type to be 'AngrySlug'.
                self.annotate_position(slug_position, 'Angry\nSlug')
            elif isinstance(slug, ScaredSlug):
                #Put the notation of slug type to be 'ScaredSlug'.
                self.annotate_position(slug_position, 'Scared\nSlug')


class DungeonInfo(AbstractGrid): #One class in view
    def __init__(self,
        master: Union[tk.Tk, tk.Frame],
        dimensions: tuple[int, int],
        size: tuple[int, int],
        **kwargs,
    ) -> None:
        """
        Constructor for DungeonInfo class.

        Parameters:
            master: The master widget.
            dimensions: A tuple of the rows and columns of the info part.
            size: A tuple of the size of the info part in pixel.
        """

        super().__init__(master, dimensions, size, **kwargs)




    def redraw(self, entities: dict[Position, Entity]) -> None:
        """
        Redraws the entities' infos.

        Parameters:
            entities: A dictionary of positions and the Entity.
        """
        self.clear()
        #Set the default value of the slug number.
        slugs_num = 1

        #Draw the title of the info part.
        self.annotate_position((0,0), text='Name', font=TITLE_FONT)
        self.annotate_position((0,1), text='Position', font=TITLE_FONT)
        self.annotate_position((0,2), text='Weapon', font=TITLE_FONT)
        self.annotate_position((0,3), text='Health', font=TITLE_FONT)
        self.annotate_position((0,4), text='Poison', font=TITLE_FONT)




        #Use a for loop to judge all the entities in the entities dictionary.
        for entity_position, entity in entities.items():

            #If the entity is a player, draw the information of the player.
            if isinstance(entity, Player):
                player_name = 'Player'
                player_weapon = 'None'
                if entity.get_weapon() is not None:
                    player_weapon = entity.get_weapon().get_name()
                player_health = entity.get_health()
                player_poison = entity.get_poison()

                #Draw the player's information on the Player_info part.
                self.annotate_position((1,0), text=player_name, font=REGULAR_FONT)
                self.annotate_position((1,1), text=str(entity_position), font=REGULAR_FONT)
                self.annotate_position((1,2), text=player_weapon, font=REGULAR_FONT)
                self.annotate_position((1,3), text=str(player_health), font=REGULAR_FONT)
                self.annotate_position((1,4), text=str(player_poison), font=REGULAR_FONT)


            #If the entity is a slug, draw the information of the slug.
            elif isinstance(entity, Slug):
                slug_name = str(entity)
                slug_weapon = entity.get_weapon().get_name()
                slug_health = entity.get_health()
                slug_poison = entity.get_poison()

                #Draw the slugs' information on the Slug_info part.
                self.annotate_position((slugs_num,0), text=slug_name, font=REGULAR_FONT)
                self.annotate_position((slugs_num,1), text=str(entity_position), font=REGULAR_FONT)
                self.annotate_position((slugs_num,2), text=slug_weapon, font=REGULAR_FONT)
                self.annotate_position((slugs_num,3), text=str(slug_health), font=REGULAR_FONT)
                self.annotate_position((slugs_num,4), text=str(slug_poison), font=REGULAR_FONT)


                #Add the slug number by 1 for the next slug's info
                #to be drawn on the next row.
                slugs_num += 1



class ButtonPanel(tk.Frame):
    def __init__(self, root:tk.Tk, on_load: Callable, on_quit: Callable) -> None:
        """
        Constructor for ButtonPanel class.

        Parameters:
            root: The Tk instance.
            on_load: The function called when click the Load Game button.
            on_quit: The function called when click the Quit button.
        """

        super().__init__(root)
        self._root = root
        #Pack the button panel to the top of the root window as it can.
        self.pack(side=tk.TOP)

        #Creater a frame for the load button.
        load_button_panel = tk.Frame(
            self,
            bg='Grey',
            width=DUNGEON_MAP_SIZE[0]
        )
        load_button_panel.pack(side=tk.LEFT, fill='both', expand=True)

        #Create the load game button.
        load_button = tk.Button(
            load_button_panel,
            text='Load Game',
            command=on_load,
            bg='White'
        )
        load_button.pack(fill='both', expand=True)

        #Create a frame for the quit button.
        quit_button_panel = tk.Frame(
            self,
            bg='Grey',
            width=SLUG_INFO_SIZE[0]
        )
        quit_button_panel.pack(side=tk.LEFT, fill='both', expand=True)

        #Create the quit button.
        quit_button = tk.Button(
            quit_button_panel,
            text='Quit',
            command=on_quit,
            bg='White'
        )
        quit_button.pack(fill='both', expand=True)



class SlugDungeon(): #Controller
    """
    A class to display the SlugDungeon game.
    """

    def __init__(self, root: tk.Tk, filename: str) -> None:
        """
        Constructor for SlugDungeon class.

        Parameters:
            root: The Tk instance.
            filename: The name of the file to read.
        """

        #Set the root (window) and the title of the game.
        self._root = root
        self._root.title('Slug Dungeon')
        #Read the file input and load the model.
        self._filename = filename
        self._model = load_level(filename)

        #Set the game frame (map and slugs info).
        self._game_frame = tk.Frame(root)
        self._game_frame.pack(side=tk.TOP)
        #Set the dungeon map inside the game frame.
        self._dungeon_map = DungeonMap(
            self._game_frame,
            self._model.get_dimensions(),
            size=DUNGEON_MAP_SIZE
        )
        self._dungeon_map.pack(side=tk.LEFT,fill='both')
        self._dungeon_map.redraw(self._model.get_tiles(),
                                      self._model.get_player_position(),
                                      self._model.get_slugs())
        #Set the slugs info inside the game frame.
        self._slugs_info = DungeonInfo(
            self._game_frame,
            (7,5),
            SLUG_INFO_SIZE
        )
        self._slugs_info.pack(side=tk.LEFT, fill='both', expand=True)
        self._slugs_info.redraw(self._model.get_slugs())

        #Set the player info widget.
        self._player_info = DungeonInfo(
            self._root,
            (2,5),
            PLAYER_INFO_SIZE
        )
        self._player_info.pack(side=tk.TOP)
        self._player_info.redraw(
            {self._model.get_player_position(): self._model.get_player()}
        )

        #Set the button panel.
        self._button_panel = ButtonPanel(
            self._root,
            self.on_load,
            self.on_quit
        )
        self._button_panel.pack(side=tk.TOP, fill=tk.X, expand=True)

        # Bind the pressed keys with events.
        self._root.bind('<w>', self.handle_key_press)
        self._root.bind('<a>', self.handle_key_press)
        self._root.bind('<s>', self.handle_key_press)
        self._root.bind('<d>', self.handle_key_press)
        self._root.bind('<space>', self.handle_key_press)


    def redraw(self) -> None:
        """
        Redraws the game.
        """

        #Redraw the dungeon map, slugs info and player info.
        self._dungeon_map.redraw(self._model.get_tiles(),
                                      self._model.get_player_position(),
                                      self._model.get_slugs())
        self._slugs_info.redraw(self._model.get_slugs())
        self._player_info.redraw(
            {self._model.get_player_position(): self._model.get_player()}
        )

        #Update the game progress.
        self._root.update_idletasks()


    def handle_key_press(self, event: tk.Event) -> None:
        """
        Handle the input key press events.

        Parameters:
            event: The event object.
        """

        #Get the key pressed.
        key_pressed = event.keysym

        #Handle the player's move according to the key pressed.
        if key_pressed == 'w':
            self._model.handle_player_move(POSITION_DELTAS[3])
        elif key_pressed == 'a':
            self._model.handle_player_move(POSITION_DELTAS[1])
        elif key_pressed == 's':
            self._model.handle_player_move(POSITION_DELTAS[2])
        elif key_pressed == 'd':
            self._model.handle_player_move(POSITION_DELTAS[0])
        elif key_pressed == 'space':
            self._model.handle_player_move((0,0))

        #Redraw the game display after the player's move.
        self.redraw()

        #Determine if the player has won or lost.
        if self._model.has_won():
            won_message = messagebox.askyesno(WIN_TITLE, WIN_MESSAGE)
            if won_message:
                self.clear_root_window()
                SlugDungeon(self._root, self._filename)
            else:
                self._root.destroy()
        elif self._model.has_lost():
            lost_message = messagebox.askyesno(LOSE_TITLE, LOSE_MESSAGE)
            if lost_message:
                self.clear_root_window()
                SlugDungeon(self._root, self._filename)
            else:
                self._root.destroy()


    def load_level(self) -> None:
        """
        Load the game.
        """

        #Ask for new filename input.
        self._filename = filedialog.askopenfilename()
        #Clear the root window.
        self.clear_root_window()
        #Initialize the game with the new file on the cleared root window.
        self.__init__(self._root, self._filename)



    def on_load(self) -> None: #Function for button
        """
        Load the game.
        """
        self.load_level()


    def on_quit(self) -> None: #Function for button
        """
        Quit the game.
        """
        self._root.destroy()


    def clear_root_window(self) -> None:
        """
        Clear the root window for further use.
        """

        #Destroy all the widgets in the root window
        for widget in self._root.winfo_children():
            widget.destroy()




if __name__ == "__main__":
    main()



