from abc import ABC, abstractmethod
from characters import Character, Mage

class Weapon(ABC):
    def __init__(self, name: str, damage: int):
        # Common attributes shared by all weapons
        self.name = name
        self.damage = damage

    @abstractmethod
    def save(self, filename: str) -> None:
        # Forces subclasses to implement file saving
        pass


class MeleeWeapon(Weapon):
    def __init__(self, name: str, damage: int):
        super().__init__(name, damage)

    def __repr__(self) -> str:
        # String format used for saving and debugging
        return f"MeleeWeapon,{self.name},{self.damage}"
    
    def save(self, filename: str) -> None:
        # Saves melee weapon data in CSV format to file
        with open(filename, "a") as file:
            file.write(self.__repr__() + "\n")

class RangedWeapon(Weapon):
    def __init__(self, name: str, damage: int, range: int):
        super().__init__(name, damage)
        # Ranged weapon-specific attribute: range
        self.range = range

    def __repr__(self) -> str:
        # String format used for saving and debugging
        return f"RangedWeapon,{self.name},{self.damage},{self.range}"
    
    def save(self, filename: str) -> None:
        # Saves ranged weapon data in CSV format to file
        with open(filename, "a") as file:
            file.write(self.__repr__() + "\n")

class MagicWeapon(Weapon):
    def __init__(self, name: str, damage: int, cost: int):
        super().__init__(name, damage)
        # Magic weapon-specific attribute: mana cost
        self.cost = cost

    def __repr__(self) -> str:
        # String format used for saving and debugging
        return f"MagicWeapon,{self.name},{self.damage},{self.cost}"
    
    def save(self, filename: str) -> None:
        # Saves magic weapon data in CSV format to file
        with open(filename, "a") as file:
            file.write(self.__repr__() + "\n")


def attack(attacker: Character, weapon: Weapon, target: Character, distance: int) -> None:
    # Only Mages can use magic weapons.
    if isinstance(weapon, MagicWeapon) and not isinstance(attacker, Mage):
        raise TypeError("Only Mages can use a MagicWeapon.")

    # Weapons need a range attribute to attack from a distance.
    if distance > 0 and not hasattr(weapon, "range"):
        raise ValueError("Weapons without a range cannot be used at distances greater than 0.")

    # Any weapon with a range must stay within that range.
    if hasattr(weapon, "range") and distance > weapon.range:
        raise ValueError("The target is beyond the weapon's range.")

    # Reduce target's health by weapon's damage
    target.health -= weapon.damage
    print(f"{attacker.name} attacks {target.name} with {weapon.name}, dealing {weapon.damage} damage!")
    print(f"{target.name}'s remaining health: {target.health}")
