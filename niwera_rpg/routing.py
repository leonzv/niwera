from django.urls import path
from .consumers import StoryConsumer

websocket_urlpatterns = [
    path('ws/stories/<int:story_id>/', StoryConsumer.as_asgi()),
]
