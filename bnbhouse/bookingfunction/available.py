import datetime
from bnbhouse.models import House, Bookings

# Too check if the room in availabile


def check_availabile(house, check_in, check_out):
    availabile_list = []
    booking_list = Bookings.objects.all()
    for booking in booking_list:
        if booking.check_in < check_out or booking.check_out > check_in:
            availabile_list.append(True)
        else:
            availabile_list.append(False)
    return all(availabile_list)
