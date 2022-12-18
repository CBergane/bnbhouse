from . import views
from .views import HouseListView, BookingList, HouseDetailView, \
    IndexView
from django.urls import path

app_name = 'bnbhouse'


urlpatterns = [
    path('house_list_view/',
         HouseListView,
         name='HouseListView'),
    path('home/',
         IndexView.as_view(),
         name='IndexView'),
    path('booking_list/',
         BookingList.as_view(),
         name='BookingList'),
    path('house/<category>',
         HouseDetailView.as_view(),
         name='HouseDetailView'),
    path('cancel_booking/<bookings_id>',
         views.cancel_booking,
         name='cancel_booking'),
    path('update_booking/<bookings_id>', views.update_booking, name='update_booking'),
]
