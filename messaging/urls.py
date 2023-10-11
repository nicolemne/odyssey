from django.urls import path
from .views import MessageListCreateView, MessageDetailView

urlpatterns = [
    path('messages/', MessageListCreateView.as_view(), name='message-list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
]