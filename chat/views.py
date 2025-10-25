from chat.models import Message, Room
from chat.serializers import MessageSerializer, RoomSerializer

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


def index(request):
    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})


@login_required
def room(request, room_id):
    try:
        room = request.user.rooms_joined.get(id=room_id)

    except Room.DoesNotExist:
        error_message = 'No tiene permisos de acceso a este Chat.'
        return render(
            request, 'chat/index.html',
            {
                'error_message': error_message,
                'rooms': Room.objects.all()
            }
        )

    return render(
        request,
        'chat/room.html',
        {
            'room': room,
            'messages': Message.objects.all()
        }
    )

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
