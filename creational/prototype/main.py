from abc import ABC, abstractmethod


class Copyable(ABC):
    @abstractmethod
    def clone(self) -> "Copyable":
        """Return a new object with the same state."""
        raise NotImplementedError


class GameCharacter(Copyable):
    def __init__(self, id: int, name: str, level: int, weapon: str) -> None:
        self._id = id
        self._name = name
        self._level = level
        self._weapon = weapon

    def clone(self) -> "GameCharacter":
        return GameCharacter(self._id, self._name, self._level, self._weapon)

    def get_id(self) -> int:
        return self._id

    def set_id(self, id: int) -> None:
        self._id = id

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_level(self) -> int:
        return self._level

    def set_level(self, level: int) -> None:
        self._level = level

    def get_weapon(self) -> str:
        return self._weapon

    def set_weapon(self, weapon: str) -> None:
        self._weapon = weapon

    def __str__(self) -> str:
        return (
            f"GameCharacter(id={self._id}, name='{self._name}', "
            f"level={self._level}, weapon='{self._weapon}')"
        )


class CharacterFactory:
    def __init__(self, character: GameCharacter) -> None:
        self._character = character

    def set_character(self, character: GameCharacter) -> None:
        self._character = character

    def clone_character(self) -> GameCharacter:
        return self._character.clone()


class GameRunner:
    @staticmethod
    def main() -> None:
        original = GameCharacter(1, "Archer", 10, "Bow")
        factory = CharacterFactory(original)

        clone_one = factory.clone_character()
        clone_one.set_name("Shadow")
        clone_one.set_level(12)
        clone_one.set_weapon("Crossbow")

        clone_two = factory.clone_character()
        clone_two.set_name("Knight")
        clone_two.set_level(15)
        clone_two.set_weapon("Sword")

        print(f"Original: {original}")
        print(f"Clone 1:  {clone_one}")
        print(f"Clone 2:  {clone_two}")
        print(f"Original is clone 1: {original is clone_one}")
        print(f"Original unchanged: {original}")


if __name__ == "__main__":
    GameRunner.main()