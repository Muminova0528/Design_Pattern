
class FlightBooking:
    def book_flight(self):
        print("Aviachiptalar muvaffaqiyatli bron qilindi.")

    def cancel_flight(self):
        print("Aviachipta broni bekor qilindi.")


class HotelBooking:
    def book_room(self):
        print("Mehmonxonadan xona muvaffaqiyatli bron qilindi.")

    def cancel_room(self):
        print("Mehmonxona broni bekor qilindi.")


class Payment:
    def make_payment(self):
        print("To'lov muvaffaqiyatli amalga oshirildi.")

    def refund_payment(self):
        print("To'lov summasi qaytarildi.")


class TravelFacade:
    def __init__(self):
        self.flight = FlightBooking()
        self.hotel = HotelBooking()
        self.payment = Payment()

    def book_trip(self):
        print("\n    SAYOHATNI BRON QILISH    ")

        self.flight.book_flight()
        self.hotel.book_room()
        self.payment.make_payment()

        print("Sayohat muvaffaqiyatli tashkil qilindi!")

    def cancel_trip(self):
        print("\n    SAYOHATNI BEKOR QILISH    ")

        self.flight.cancel_flight()
        self.hotel.cancel_room()
        self.payment.refund_payment()

        print("Sayohat bekor qilindi!")


travel = TravelFacade()

travel.book_trip()
travel.cancel_trip()
