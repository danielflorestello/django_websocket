from chat.views import index, room
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('room/<int:room_id>/', room, name='room'),
]
