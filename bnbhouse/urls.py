from . import views
from .views import HouseList, BookingList
from django.urls import path

app_name = 'bnbhouse'


urlpatterns = [
    path('house_list/', HouseList.as_view(), name='HouseList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
]
