from django.contrib import admin
from .models import Reservation, RoomReservationInfo


class RoomReservationInfoInline(admin.TabularInline):
    model = RoomReservationInfo
    extra = 3


class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    inlines = (RoomReservationInfoInline,)


admin.site.register(Reservation, ReservationAdmin)
