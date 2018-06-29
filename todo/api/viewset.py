from . import serializers
from todo.core import models
from rest_framework import viewsets


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    http_methods_names = ['get', 'post', 'head', 'put', 'patch']
