from django.contrib.auth.models import User, Group
from rest_framework import serializers

from . models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippets, Todo


class SnippetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = ['id', 'title', 'code', 'linones', 'languages', 'style']


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'
