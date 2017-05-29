from django.contrib import admin
from .models import User
from reservations.models import Reservation


class ReservationInline(admin.TabularInline):
    model = Reservation
    fk_name = 'customer'
    extra = 3


class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = (ReservationInline,)


admin.site.register(User, UserAdmin)
