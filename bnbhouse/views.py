from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, FormView, View
from django.views import generic
from django.urls import reverse
from .models import House, Bookings
from .booking_form import Availabilety
from bnbhouse.bookingfunction.available import check_availabile


class IndexView(TemplateView):
    template_name = "index.html"


def HouseListView(request):
    house = House.objects.all()[0]
    house_categories = dict(house.HOUSE_CATAGORIES)
    house_values = house_categories.values()
    house_list = []
    for house_category in house_categories:
        house = house_categories.get(house_category)
        house_url = reverse('bnbhouse:HouseDetailView', kwargs={
            'category': house_category})
        house_list.append((house, house_url))
    context = {
        'house_list': house_list,
    }
    return render(request, 'house_list_view.html', context)


class BookingList(ListView):
    model = Bookings

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Bookings.objects.all()
            return booking_list
        else:
            booking_list = Bookings.objects.filter(user=self.request.user)
            return booking_list


def description_list(request, slug):
    description = House.objects.get(slug=slug)
    return render(request, 'house_detail_view.html', {
        'house': house})
    print(description_list)


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

        availabile_house_list = []
        for house in house_list:
            if check_availabile(house, data['check_in'], data['check_out']):
                availabile_house_list.append(house)

        if len(availabile_house_list) > 0:
            house = availabile_house_list[0]
            booking = Bookings.objects.create(
                user=self.request.user,
                house=house,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All of this category is booked')


class BookingView(FormView):
    form_class = Availabilety
    template_name = 'booking_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        house_list = House.objects.filter(category=data['house_category'])
        availabile_house_list = []
        for house in house_list:
            if check_available(house, data['check_in'], data['check_out']):
                availabile_house_list.append(house)

        if len(availabile_house_list) > 0:
            house = availabile_house_list[0]
            booking = Bookings.objects.create(
                user=self.request.user,
                house=house,
                check_in=data['chck_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All of this category is booked')
