from file_system import FileSystem

class Folder(FileSystem):

    def __init__(self, name: str) -> None:
        self.name = name
        self.children: list[FileSystem] = []

    def add(self, item: FileSystem) -> None:
        self.children.append(item)

    def remove(self, item: FileSystem) -> None:
        if item in self.children:
            self.children.remove(item)

    def show(self) -> None:
        print(f"{self.name}/")

        for item in self.children:
            item.show()