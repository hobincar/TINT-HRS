from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rooms.models import Room

@login_required
def reservation(request):
    rooms = Room.objects.order_by('cost_per_night')
    return render(request, 'reservations/reservation.html', {'rooms': rooms})
