from django.urls import path

from .views import (
    TaskListCreate, 
    TaskRetrieveUpdateDestroy,
    StepListCreate,
    StepRetrieveUpdateDestroy
)

app_name = 'tasks'

urlpatterns = [
    path('', TaskListCreate.as_view(), name='task-list-create'),
    path('<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), 
         name='task-retrieve-update-destroy'),
    path('<int:task_pk>/steps/', StepListCreate.as_view(), 
         name='step-list-create'),
    path('<int:task_pk>/steps/<int:pk>/', StepRetrieveUpdateDestroy.as_view(), 
         name='step-retrieve-update-destroy'),
]