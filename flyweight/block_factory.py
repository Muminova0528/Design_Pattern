from block_type import BlockType


class BlockFactory:

    _block_types = {}

    @classmethod
    def get_block_type(cls, name):

        if name in cls._block_types:
            return cls._block_types[name]

        block_data = {
            "Grass": ("grass.png", "Green"),
            "Stone": ("stone.png", "Gray"),
            "Dirt": ("dirt.png", "Brown"),
            "Water": ("water.png", "Blue")
        }

        if name not in block_data:
            raise ValueError(f"Unknown block type: {name}")

        texture, color = block_data[name]

        new_type = BlockType(name, texture, color)

        cls._block_types[name] = new_type

        return new_type

    @classmethod
    def get_total_types(cls):
        return len(cls._block_types)