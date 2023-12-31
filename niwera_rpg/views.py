from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Story
from django.contrib.auth import logout, authenticate, login


def home(request):
    return render(request, 'home.html')


def logout(request):
    logout(request)


def stories(request):

    stories = Story.objects.all()

    context = {
        'stories': stories
    }
    return render(request, 'stories.html', context)


def story_details(request, story_id):
    story = Story.objects.get(id=story_id)
    connected_characters = story.character_set.all()

    context = {
        'story': story,
        'connected_characters': connected_characters
    }
    return render(request, 'story_details.html', context)
