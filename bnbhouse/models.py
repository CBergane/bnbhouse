from django.db import models
from django.urls import path, reverse_lazy
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
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return f'{self.number}. {self.category}'\
            f' with {self.beds} beds for {self.capacity} people'

    class Meta:
        ordering: ('number')


class Bookings(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    slug = models.SlugField()

    def __str__(self):
        return f'{self.user} has booked {self.house} '
        f'from {self.check_in} untill {self.check_out}'

    def get_house_category(self):
        house_categories = dict(self.house.HOUSE_CATAGORIES)
        house_category = house_categories.get(self.house.category)
        return house_category

    def get_cancel_booking_url(self):
        return reverse_lazy('bnbhouse:CancelBooking', args=[self.pk, ])
