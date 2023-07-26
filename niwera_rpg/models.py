from django.db import models
from django.contrib.auth.models import User


class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    hp = models.IntegerField()
    xp = models.IntegerField()
    level = models.IntegerField()
    mana = models.IntegerField()
    money = models.DecimalField(max_digits=10, decimal_places=2)
    stories = models.ManyToManyField('Story', through='CharacterStory')
    # outros campos do personagem

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Personagem'
        verbose_name_plural = 'Personagens'


class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    # outros campos da história

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'História'
        verbose_name_plural = 'Histórias'


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'


class CharacterStory(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    # outros campos da relação personagem-história

    def __str__(self):
        return f'{self.character} - {self.story}'

    class Meta:
        verbose_name = 'Personagem na História'
        verbose_name_plural = 'Personagens na História'
