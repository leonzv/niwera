from django.shortcuts import render
from django.http import HttpResponse
from .models import Story


def stories(request):

    stories = Story.objects.all()

    context = {
        'stories': stories
    }
    return render(request, 'stories.html', context)


def story_details(request, story_id):
    story_data = {...}  # Dados da história
    connected_characters = [...]  # Lista de personagens conectados

    return render(request, 'story_details.html', {'story_data': story_data, 'connected_characters': connected_characters})
