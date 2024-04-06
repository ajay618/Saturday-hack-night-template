from . import views
from django.urls import path

urlpatterns = [
    path('addtask/', views.addTask, name='addTask'),
    path('marks_as_done/<int:pk>/' , views.mark_as_done , name="mark_as_done"),
    path('marks_as_undone/<int:pk>/' , views.mark_as_undone , name="mark_as_undone"),
    path('edit_task/<int:pk>/' , views.edit_task , name="edit_task"),
]
