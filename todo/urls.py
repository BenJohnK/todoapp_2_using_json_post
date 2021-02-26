from django.urls import path,include
import todo.urls
from .views import home,titlesubmit

urlpatterns = [
    path('',home,name="home"),
    path('titlesubmit/',titlesubmit,name="titlesubmit"),
]