from cms import Cms
from website_builder import WebsiteBuilder


class SimpleWebsiteBuilder(WebsiteBuilder):
    def build_name(self) -> "SimpleWebsiteBuilder":
        self.get_website().name = "Simple Website Builder"
        return self

    def build_cms(self) -> "SimpleWebsiteBuilder":
        self.get_website().cms = Cms.TILDA
        return self

    def build_price(self) -> "SimpleWebsiteBuilder":
        self.get_website().price = 500
        return self
