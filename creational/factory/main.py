class Latte:
    def name(self):
        return "Латте"


class Tea:
    def name(self):
        return "Чай"

class DrinkFactory:
    def create_drink(self, kind):
        if kind == "coffee":
            return Latte()
        elif kind == "tea":
            return Tea()
        else:
            raise ValueError(f"Unknown drink: {kind}")


class Cafe:
    def __init__(self):
        self.factory = DrinkFactory()

    def order(self, kind):
        drink = self.factory.create_drink(kind)
        print(f"Готовим и выдаём: {drink.name()}")

cafe = Cafe()

cafe.order("coffee")
cafe.order("tea")