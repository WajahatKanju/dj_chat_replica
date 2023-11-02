from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room


@login_required
def rooms(request):
    all_rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': all_rooms})


@login_required()
def room(request, slug):
    current_room = Room.objects.get(slug=slug)
    return render(request, 'room/room.html', {'room': current_room})
