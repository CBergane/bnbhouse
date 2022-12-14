from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import house, Bookings


class IndexView(TemplateView):
    template_name = "index.html"


class HouseList(ListView):
    model = house


class BookingList(ListView):
    model = Bookings
