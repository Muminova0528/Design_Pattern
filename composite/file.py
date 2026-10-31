from file_system import FileSystem


class File(FileSystem):

    def __init__(self, name: str) -> None:
        self.name = name

    def show(self) -> None:
        print(self.name)