from django.contrib import admin
from .models import Character, Story, Status, CharacterStory

admin.site.register(Character)
admin.site.register(Story)
admin.site.register(Status)
admin.site.register(CharacterStory)

