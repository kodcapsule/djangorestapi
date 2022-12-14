from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from datetime import datetime

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
# print(LEXERS)S

# Create your models here.


class Snippets(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linones = models.BooleanField(default=False)
    languages = models.CharField(
        choices=LANGUAGE_CHOICES, default='Python', max_length=100)
    style = models.CharField(
        max_length=100, choices=STYLE_CHOICES, default="Friendly")

    # class Meta:
    #     odering = ['created']


class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False, default="others")
    description = models.TextField(default="TODO item")
    created = models.DateField(default=datetime.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
