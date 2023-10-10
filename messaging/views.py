from rest_framework import generics, permissions
from .models import Message
from .serializers import MessageSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    """
    View to list and create messages.
    """
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Retrieve messages sent by or received by the authenticated user
        user = self.request.user
        return Message.objects.filter(owner=user) | Message.objects.filter(receiver=user)

    def perform_create(self, serializer):
        # Set the message sender to the authenticated user
        serializer.save(owner=self.request.user)

class MessageDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single message by its ID.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]