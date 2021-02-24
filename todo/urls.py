from django.urls import path,include
import todo.urls
from .views import home

urlpatterns = [
    path('',home,name="home")
]