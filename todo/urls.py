from . import views
from django.urls import path

urlpatterns = [
    path('addtask/', views.addTask, name='addTask'),
    path('marks_as_done/<int:pk>/' , views.mark_as_done , name="mark_as_done")
]
