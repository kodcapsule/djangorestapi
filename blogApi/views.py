from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def blogPost(request):
    return HttpResponse('Welcome to the blog post API')