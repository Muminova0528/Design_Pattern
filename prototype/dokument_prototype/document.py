
from copy import deepcopy
from copyable import Copyable


class Document(Copyable):

    def __init__(
        self,
        id: int,
        title: str,
        content: str,
        author: str,
        tags: list[str]
    ) -> None:
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        self.tags = tags

    def clone(self) -> "Document":
        return deepcopy(self)

    def display(self) -> None:
        print(f"ID: {self.id}")
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")
        print(f"Author: {self.author}")
        print(f"Tags: {self.tags}")
        print("-" * 40)
