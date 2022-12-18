import datetime
from bnbhouse.models import House, Bookings

# Too check if the room in availabile


def check_availabile(house, check_in, check_out):
    availabile = []
    booking_list = Bookings.objects.filter(house=house)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            availabile.append(True)
        else:
            availabile.append(False)
    return all(availabile)
