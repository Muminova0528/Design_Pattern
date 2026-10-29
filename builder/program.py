from director import Director
from simple_website_builder import SimpleWebsiteBuilder


def main() -> None:
    director = Director()
    director.set_website(SimpleWebsiteBuilder())
    print(director.build_website())


if __name__ == "__main__":
    main()
