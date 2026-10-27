from dataclasses import dataclass
from typing import Optional

from cms import Cms


@dataclass
class Website:
    name: str = ""
    cms: Optional[Cms] = None
    price: int = 0

    def __str__(self) -> str:
        cms = self.cms.name if self.cms is not None else "None"
        return f"Website{{name='{self.name}', cms={cms}, price={self.price}}}"
