from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponse


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from RestAPIs import client
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
# from .serializers import UserSerializer, GroupSerializer
# Create your views here.

from django.shortcuts import get_object_or_404

from . serializers import SnippetsSerializer, TodoSerializer
from . models import Todo


from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


def clientApp(request):
    resp = client.getRequest('https://httpbin.org/anything')
    print(request.body)
    return HttpResponse(resp)


@api_view(['GET'])
def index(request):
    api_url = {
        'description': 'This is a list of all the urls that are available in the API',
        'todo-lists': 'api/todo-items/',
        'todo-item-details': 'api/todo-item/<int:pk>/',
        'Create Todo Item': 'api/create-todo-item/',
        'Update Todo Item': 'api/update-todo/<int:pk>/',
        'Delete Todo Item': 'api/delete-todo-item/<int:pk>/',
    }

    return Response(api_url)


@api_view(['GET'])
def todoList(request):
    todos = Todo.objects.all()
    todose = TodoSerializer(todos, many=True)
    # print(todos)
    # print(todose.data)
    return Response(todose.data)


# Class based views

class TodoListView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


@api_view(['GET'])
def getTodoDetails(request, pk):
    todo = Todo.objects.get(id=pk)
    todoser = TodoSerializer(todo, many=False)
    return Response(todoser.data)


@api_view(['POST'])
def createTodo(request):
    todoserilizer = TodoSerializer(data=request.data)
    if todoserilizer.is_valid():
        todoserilizer.save()
    return Response(todoserilizer.data)


class CreateTodoItem(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        todo = get_object_or_404(Todo, id=self.request.data.get('id'))
        return serializer.save(todo=todo)


@api_view(['POST'])
def updateTodo(request, pk):
    todoitem = Todo.objects.get(id=pk)
    todoitemSerilizer = TodoSerializer(instance=todoitem, data=request.data)
    if todoitemSerilizer.is_valid():
        todoitemSerilizer.save()
    return Response(todoitemSerilizer.data)


@api_view(['DELETE'])
def deleteTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response('Item  deleted successfully')
