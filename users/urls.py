from django.urls import path
from .views import index, add

urlpatterns = [
    path("", index, name="bienvenida"),
    path("add", add, name="add"),
]
