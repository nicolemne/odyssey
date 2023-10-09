from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    """
    Custom model for messaging in the app
    """
    owner = models.ForeignKey(
        User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        User, related_name='received_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    class Meta: 
        ordering = ['created_at']

    def __str__(self):
        return f"From {self.owner.username} to {self.receiver.username} - {self.created_at}"