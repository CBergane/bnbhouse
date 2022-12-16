from . import views
from .views import HouseListView, BookingList, BookingView, HouseDetailView, IndexView, description_list
from django.urls import path

app_name = 'bnbhouse'


urlpatterns = [
    path('house_list_view/', HouseListView, name='HouseListView'),
    path('home/', IndexView.as_view(), name='IndexView'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('bookings/', BookingView.as_view(), name='Bookingview'),
    path('house/<category>', HouseDetailView.as_view(), name='HouseDetailView'),
]
