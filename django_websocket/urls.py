from chat.views import MessageViewSet, RoomViewSet

from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'room', RoomViewSet, basename='room')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('chat.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
