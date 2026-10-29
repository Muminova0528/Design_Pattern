
from abc import ABC, abstractmethod


class Copyable(ABC):
    @abstractmethod
    def clone(self) -> "Copyable":
        pass


class GameCharacter(Copyable):
    def __init__(self, id, name, level, weapon):
        self._id = id
        self._name = name
        self._level = level
        self._weapon = weapon

    def clone(self):
        return GameCharacter(self._id, self._name, self._level, self._weapon)

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_weapon(self):
        return self._weapon

    def set_id(self, id):
        self._id = id

    def set_name(self, name):
        self._name = name

    def set_level(self, level):
        self._level = level

    def set_weapon(self, weapon):
        self._weapon = weapon

    def __str__(self):
        return f"GameCharacter(id={self._id}, name='{self._name}', level={self._level}, weapon='{self._weapon}')"


class CharacterFactory:
    def __init__(self, character):
        self._character = character

    def setCharacter(self, character):
        self._character = character

    def cloneCharacter(self):
        return self._character.clone()


class GameRunner:
    @staticmethod
    def main():
        original = GameCharacter(1, "Archer", 10, "Bow")
        factory = CharacterFactory(original)

        clone1 = factory.cloneCharacter()
        clone1.set_name("Shadow")
        clone1.set_level(12)
        clone1.set_weapon("Crossbow")

        clone2 = factory.cloneCharacter()
        clone2.set_name("Knight")
        clone2.set_level(15)
        clone2.set_weapon("Sword")

        print("Original:", original)
        print("Clone 1:", clone1)
        print("Clone 2:", clone2)

        print(original is clone1)
        print(original is clone2)
        print(clone1 is clone2)


if __name__ == "__main__":
    GameRunner.main()
