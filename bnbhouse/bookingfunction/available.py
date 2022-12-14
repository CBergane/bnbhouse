import datetime
from bnbhouse.models import house, Bookings

# Too check if the room in available


def check_available(house, check_in, check_out):
    available = []
    booking_list = Bookings.objects.filter(house=house)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            available.append(True)
        else:
            available.append(False)
    return all(available)
