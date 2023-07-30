from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stories/', views.stories, name='stories'),
    path('<int:story_id>/',
         views.story_details, name='story_details'),
]
