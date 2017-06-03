from django.shortcuts import render
from rooms.models import Room


def main(request):
    rooms = Room.objects.all()
    return render(request, 'main.html', {'rooms': rooms})
