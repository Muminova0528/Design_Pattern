
from abc import ABC, abstractmethod


# 1. Copyable interface
class Copyable(ABC):
    @abstractmethod
    def clone(self) -> "Copyable":
        pass


# 2. GameCharacter class
class GameCharacter(Copyable):
    def __init__(self, id: int, name: str, level: int, weapon: str) -> None:
        self._id = id
        self._name = name
        self._level = level
        self._weapon = weapon

    def clone(self) -> "GameCharacter":
        return GameCharacter(
            self._id,
            self._name,
            self._level,
            self._weapon
        )

    # Getters
    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_level(self) -> int:
        return self._level

    def get_weapon(self) -> str:
        return self._weapon

    # Setters
    def set_id(self, id: int) -> None:
        self._id = id

    def set_name(self, name: str) -> None:
        self._name = name

    def set_level(self, level: int) -> None:
        self._level = level

    def set_weapon(self, weapon: str) -> None:
        self._weapon = weapon

    # toString() equivalent in Python
    def __str__(self) -> str:
        return (
            f"GameCharacter(id={self._id}, name='{self._name}', "
            f"level={self._level}, weapon='{self._weapon}')"
        )


# 3. CharacterFactory class
class CharacterFactory:
    def __init__(self, character: GameCharacter) -> None:
        self._character = character

    def setCharacter(self, character: GameCharacter) -> None:
        self._character = character

    def cloneCharacter(self) -> GameCharacter:
        return self._character.clone()


# 4. GameRunner class
class GameRunner:
    @staticmethod
    def main() -> None:
        # Original character
        original = GameCharacter(1, "Archer", 10, "Bow")

        # Factory stores the prototype
        factory = CharacterFactory(original)

        # Create first clone
        clone_one = factory.cloneCharacter()
        clone_one.set_name("Shadow")
        clone_one.set_level(12)
        clone_one.set_weapon("Crossbow")

        # Create second clone
        clone_two = factory.cloneCharacter()
        clone_two.set_name("Knight")
        clone_two.set_level(15)
        clone_two.set_weapon("Sword")

        # Display characters
        print("Original:", original)
        print("Clone 1: ", clone_one)
        print("Clone 2: ", clone_two)

        # Verify that clones are different objects
        print("\nObject identity checks:")
        print("Original is clone 1:", original is clone_one)
        print("Original is clone 2:", original is clone_two)
        print("Clone 1 is clone 2:", clone_one is clone_two)

        # Verify that the original was not changed
        print("\nOriginal character remains unchanged:")
        print("Name:", original.get_name())
        print("Level:", original.get_level())
        print("Weapon:", original.get_weapon())


if __name__ == "__main__":
    GameRunner.main()
