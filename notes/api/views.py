from rest_framework import permissions, viewsets
from .serializers import NoteSerializer
from .models import Note
from rest_framework import permissions

    
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    def perform_authentication(self, request):
        return super().perform_authentication(request)
