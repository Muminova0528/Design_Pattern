from abc import ABC, abstractmethod
from typing import Optional

from website import Website


class WebsiteBuilder(ABC):
    def __init__(self) -> None:
        self.website: Optional[Website] = None

    def create_website(self) -> "WebsiteBuilder":
        self.website = Website()
        return self

    @abstractmethod
    def build_name(self) -> "WebsiteBuilder":
        pass

    @abstractmethod
    def build_cms(self) -> "WebsiteBuilder":
        pass

    @abstractmethod
    def build_price(self) -> "WebsiteBuilder":
        pass

    def get_website(self) -> Website:
        if self.website is None:
            raise RuntimeError("Call create_website() before get_website().")
        return self.website
