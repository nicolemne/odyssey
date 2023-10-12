from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Rating
from .serializers import RatingSerializer
from posts.models import Post
from django.db.models import Avg

class RatePostView(generics.CreateAPIView):
    """
    View to rate a post and update the average rating.
    """
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    @login_required  # Ensure the user is logged in
    def create(self, request, *args, **kwargs):
        post_id = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_id)

        # Check if the user has already rated the post
        existing_rating = Rating.objects.filter(owner=request.user, post=post).first()
        if existing_rating:
            # If the user has already rated, update their rating
            serializer = self.get_serializer(existing_rating, data=request.data)
        else:
            # If the user hasn't rated, create a new rating
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user, post=post)

        # Recalculate the average rating for the post
        average_rating = Rating.objects.filter(post=post).aggregate(Avg('rating'))['rating__avg']
        if average_rating is not None:
            post.average_rating = round(average_rating, 2)
        else:
            post.average_rating = 0.0
        post.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
