from . import views
from .views import HouseList, BookingList, BookingView, HouseDetailView
from django.urls import path

app_name = 'bnbhouse'


urlpatterns = [
    path('house_list/', HouseList.as_view(), name='HouseList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('bookings/', BookingView.as_view(), name='Bookingview'),
    path('house/<category>', HouseDetailView.as_view(), name='HouseDetailview'),
]
