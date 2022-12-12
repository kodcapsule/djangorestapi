from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BaseAuthentication

from . models import Post
from . serializers import PostSerializer
from .permissions import isAuthorOrReadOnly

# Create your views here.


class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [SessionAuthentication, BaseAuthentication]
    permission_classes = [isAuthorOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
