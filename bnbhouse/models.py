from django.db import models
from django.urls import path
from django.conf import settings


class House(models.Model):
    HOUSE_CATAGORIES = (
        ('BAS', 'BASIC'),
        ('STN', 'STANDARD'),
        ('LUX', 'LUXURIUS'),
        ('ROY', 'ROYAL'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=HOUSE_CATAGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'


class Bookings(models.Model):
    guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.guest} has booked {self.house} from {self.check_in} untill {self.check_out}'
