from django.shortcuts import render
from django.views import View

# Create your views here.

class MakeReservationView(View):
    template_name = 'ReservePC/index.html'
    #you need to be logged in to make a reservation
    #first you pick a date (every date is displayed with a color depending on the number of reservations on that day)
    #then you pick a time (every time is displayed with a color depending on the number of reservations on that time)
    #than you pick a station from the list of available stations
    #than you make a reservation
    def get(self, request):
        return render(request, self.template_name)

