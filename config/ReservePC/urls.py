from django.urls import path
from . import views


app_name = 'ReservePC'
urlpatterns = [
    path('', views.MakeReservationView.as_view(), name='index'),
]
