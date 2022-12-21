from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, FormView, \
    View, DeleteView
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import House, Bookings
from .booking_form import Availabilety
from bnbhouse.bookingfunction.available import check_availabile


class IndexView(TemplateView):
    template_name = "index.html"


def HouseListView(request):
    obj = House.objects.all().values("description").distinct()
    house = House.objects.all()[0]
    house_categories = dict(house.HOUSE_CATAGORIES)
    house_values = house_categories.values()
    house_list = []
    for house_category in house_categories:
        house = house_categories.get(house_category)
        house_url = reverse('bnbhouse:HouseDetailView', kwargs={
            'category': house_category, })
        house_list.append((house, house_url))
    context = {
        'house_list': house_list,
        'object': obj,
    }
    return render(request, 'house_list_view.html', context)


class BookingList(ListView):
    model = Bookings
    template_name = 'bookings_list.html'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Bookings.objects.all()
            return booking_list
        else:
            booking_list = Bookings.objects.filter(user=self.request.user)
            return booking_list


class HouseDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category',  None)
        form = Availabilety()
        house_list = House.objects.filter(category=category)
        if len(house_list) > 0:
            house = house_list[0]
            house_category = dict(house.HOUSE_CATAGORIES).get(
                house.category, None)
            obj = House.objects.get(category=category)
            context = {
                'house_category': house_category,
                'form': form,
                'object': obj,
            }
            return render(request, 'house_detail_view.html', context)
        else:
            return HttpResponse('Category dose not exist')

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        house_list = House.objects.filter(category=category)
        form = Availabilety(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_house = []
        for house in house_list:
            if check_availabile(house, data['check_in'], data['check_out']):
                available_house.append(house)

        if len(available_house) > 0:
            house = available_house[0]

            booking = Bookings.objects.create(
                user=self.request.user,
                house=house,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return render(request, 'index.html')

        else:
            return HttpResponse('All of this category is booked')


# Cancel booking


class CancelBooking(DeleteView):
    model = Bookings
    template_name = 'booking_cancel.html'
    success_url = reverse_lazy('bnbhouse:BookingList')
