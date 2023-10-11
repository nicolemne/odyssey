from django.urls import path
from ratings import views

urlpatterns = [
    path('ratings/rate/<int:pk>/', views.RatePostView.as_view(), name='rate-post'),
]