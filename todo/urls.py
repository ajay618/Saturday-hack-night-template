from . import views
from django.urls import path

urlpatterns = [
    path('addtask/', views.addTask, name='addTask')
]
