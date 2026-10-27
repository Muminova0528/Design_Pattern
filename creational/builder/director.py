from typing import Optional

from website import Website
from website_builder import WebsiteBuilder


class Director:
    def __init__(self) -> None:
        self.builder: Optional[WebsiteBuilder] = None

    def set_website(self, builder: WebsiteBuilder) -> None:
        self.builder = builder

    def build_website(self) -> Website:
        if self.builder is None:
            raise RuntimeError("Set a website builder before building a website.")

        return (
            self.builder
            .create_website()
            .build_name()
            .build_cms()
            .build_price()
            .get_website()
        )
