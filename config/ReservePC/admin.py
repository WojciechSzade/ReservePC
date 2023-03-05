from django.contrib import admin

from .models import User, Classroom, Station, Reservation
# Register your models here.

admin.site.register(User)
admin.site.register(Classroom)
admin.site.register(Station)
admin.site.register(Reservation)