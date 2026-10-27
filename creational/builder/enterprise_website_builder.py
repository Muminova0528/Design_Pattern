from cms import Cms
from website_builder import WebsiteBuilder


class EnterpriseWebsiteBuilder(WebsiteBuilder):
    def build_name(self) -> "EnterpriseWebsiteBuilder":
        self.get_website().name = "Enterprise Website"
        return self

    def build_cms(self) -> "EnterpriseWebsiteBuilder":
        self.get_website().cms = Cms.WORDPRESS
        return self

    def build_price(self) -> "EnterpriseWebsiteBuilder":
        self.get_website().price = 1000
        return self
