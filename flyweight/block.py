class Block:

    def __init__(self, x, y, z, block_type):
        self.x = x
        self.y = y
        self.z = z
        self.block_type = block_type

    def render(self):
        print(
            f"Block: {self.block_type.name} | "
            f"Position: ({self.x}, {self.y}, {self.z}) | "
            f"Texture: {self.block_type.texture} | "
            f"Color: {self.block_type.color}"
        )