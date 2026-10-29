
from document import Document


class DocumentFactory:

    def __init__(self, prototype: Document) -> None:
        self.prototype = prototype

    def cloneDocument(self) -> Document:
        return self.prototype.clone()
