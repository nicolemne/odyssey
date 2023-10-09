from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message
from profiles.models import Profile

class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for messages, both sender and receiver information.
    Fetches sender and receiver usernames and profile images.
    """
    sender_username = serializers.ReadOnlyField(source='owner.username')
    sender_image = serializers.SerializerMethodField()
    receiver_username = serializers.ReadOnlyField(source='receiver.username')
    receiver_image = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ('id', 'owner', 'receiver', 'created_at', 'content', 'sender_username', 'sender_image', 'receiver_username', 'receiver_image')

    def get_sender_image(self, obj):
        try:
            sender_profile = Profile.objects.get(owner=obj.owner)
            return sender_profile.image.url if sender_profile.image else '../default_profile_qdjgyp'
        
        except Profile.DoesNotExist:
            return None

    def get_receiver_image(self, obj):
        try:
            receiver_profile = Profile.objects.get(owner=obj.receiver)
            return receiver_profile.image.url if receiver_profile.image else '../default_profile_qdjgyp'
        
        except Profile.DoesNotExist:
            return None
