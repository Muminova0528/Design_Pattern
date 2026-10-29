from document import Document
from document_factory import DocumentFactory


def main() -> None:
    original = Document(
        id=1,
        title="Python Basics",
        content="Introduction to Python programming.",
        author="Anora",
        tags=["Python", "Programming", "Beginner"]
    )

    factory = DocumentFactory(original)

    document1 = factory.cloneDocument()
    document2 = factory.cloneDocument()

    document1.title = "Advanced Python"
    document1.content = "Advanced Python programming."
    document1.tags.append("Advanced")

    document2.title = "Java Basics"
    document2.content = "Introduction to Java programming."
    document2.tags[0] = "Java"

    print("ORIGINAL DOCUMENT")
    original.display()

    print("FIRST COPY")
    document1.display()

    print("SECOND COPY")
    document2.display()


if __name__ == "__main__":
    main()
