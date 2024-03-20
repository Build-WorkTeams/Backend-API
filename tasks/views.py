from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Task, Step
from .serializers import TaskSerializer, StepSerializer

# Create your views here.
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.tasks.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.tasks.all()
    
class StepListCreate(generics.ListCreateAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.get(pk=self.kwargs['task_pk']).steps.all()

    def perform_create(self, serializer):
        serializer.save(task=Task.objects.get(pk=self.kwargs['task_pk']))
        
class StepRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.get(pk=self.kwargs['task_pk']).steps.all()