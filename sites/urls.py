from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', views.clientApp, name="client"),
    path('', views.index, name="index"),
    path('api-overview/', views.TodoListView.as_view(), name="index"),
    path('api/todo-items/', views.todoList, name="todo-list"),
    path('api/create-todo-item/', views.createTodo, name="create-todo"),
    path('api/update-todo/<int:pk>/',
         views.CreateTodoItem.as_view(), name="update-todo"),
    # path('api/update-todo/<int:pk>/', views.updateTodo, name="update-todo"),
    path('api/delete-todo-item/<int:pk>/',
         views.deleteTodo, name="delete-todo"),
    path('api/todo-item/<int:pk>/', views.getTodoDetails, name="todo-list-item"),
]
