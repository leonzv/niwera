from django.urls import path
from . import views

urlpatterns = [
    path('stories/', views.stories, name='stories'),
    path('stories/<int:story_id>/',
         views.story_details, name='story_details'),
]
