from todo.api import viewset
from django.urls import include, path
from rest_framework.routers import DefaultRouter


router = DefaultRouter(trailing_slash=False)
router.register(r'todos', viewset.TodoViewSet, base_name='todos')

urlpatterns = [
    path('', include(router.urls)),
]
