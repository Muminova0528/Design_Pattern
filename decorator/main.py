
from abc import ABC, abstractmethod


class Order(ABC):

    @abstractmethod
    def getDescription(self):
        pass

    @abstractmethod
    def getPrice(self):
        pass


class BasicOrder(Order):

    def getDescription(self):
        return "Oddiy buyurtma"

    def getPrice(self):
        return 100000


class OrderDecorator(Order):

    def __init__(self, order):
        self.order = order

    def getDescription(self):
        return self.order.getDescription()

    def getPrice(self):
        return self.order.getPrice()


class GiftWrapDecorator(OrderDecorator):

    def getDescription(self):
        return self.order.getDescription() + " + Sovg'a qadoqlash"

    def getPrice(self):
        return self.order.getPrice() + 15000


class ExpressDeliveryDecorator(OrderDecorator):

    def getDescription(self):
        return self.order.getDescription() + " + Tezkor yetkazib berish"

    def getPrice(self):
        return self.order.getPrice() + 25000


order = BasicOrder()

print("Oddiy buyurtma:")
print(order.getDescription())
print("Narxi:", order.getPrice(), "so'm")

print("\nSovg'a qadoqlash bilan:")
gift_order = GiftWrapDecorator(order)
print(gift_order.getDescription())
print("Narxi:", gift_order.getPrice(), "so'm")

print("\nTezkor yetkazib berish bilan:")
express_order = ExpressDeliveryDecorator(order)
print(express_order.getDescription())
print("Narxi:", express_order.getPrice(), "so'm")

print("\nIkkala xizmat bilan:")
full_order = ExpressDeliveryDecorator(
    GiftWrapDecorator(order)
)
print(full_order.getDescription())
print("Narxi:", full_order.getPrice(), "so'm")
