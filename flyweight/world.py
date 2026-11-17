from block import Block
from block_factory import BlockFactory


class World:

    def __init__(self):
        self.blocks = []

    def add_block(self, x, y, z, block_name):

        block_type = BlockFactory.get_block_type(block_name)

        block = Block(x, y, z, block_type)

        self.blocks.append(block)

    def render(self):

        print("===== MINECRAFT WORLD =====")

        for block in self.blocks:
            block.render()

        print("---------------------------")
        print(f"Total blocks: {len(self.blocks)}")
        print(f"Unique BlockTypes: {BlockFactory.get_total_types()}")

    def check_same_type(self, first, second):

        return (
            self.blocks[first].block_type
            is self.blocks[second].block_type
        )


if __name__ == "__main__":

    world = World()

    world.add_block(0, 0, 0, "Grass")
    world.add_block(1, 0, 0, "Grass")
    world.add_block(2, 0, 0, "Stone")
    world.add_block(3, 0, 0, "Grass")
    world.add_block(4, 0, 0, "Dirt")

    world.render()

    print("\n===== FLYWEIGHT TEST =====")

    print("Grass == Grass:", world.check_same_type(0, 1))
    print("Grass == Grass:", world.check_same_type(0, 3))
    print("Grass == Stone:", world.check_same_type(0, 2))