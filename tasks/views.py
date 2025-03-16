from rest_framework import generics, permissions, filters
from .models import Task
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['priority', 'status', 'due_date']  # Allow filtering by these fields
    ordering_fields = ['due_date', 'priority']  # Allow sorting
    search_fields = ['title', 'description']  # Allow searching by these fields

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)

# Retrieve, Update, and Delete a Task
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)
