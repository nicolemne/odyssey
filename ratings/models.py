from django.db import models
from posts.models import Post
from django.contrib.auth.models import User

class Rating(models.Model):
    """
    Rating model for posts, storing average ratings and related data
    """
    post = models.OneToOneField(Post, related_name='rating', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rating = models.PositiveIntegerField(default=1, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    def __str__(self):
        rating_text = self.get_rating_text()
        return f'Average rating: {self.average_rating} {rating_text}'

    def get_rating_text(self):
        if self.average_rating >= 4.5:
            return 'Excellent'
        elif self.average_rating >= 3.5:
            return 'Good'
        elif self.average_rating >= 2.5:
            return 'Average'
        elif self.average_rating >= 1.5:
            return 'Below Average'
        else:
            return 'Poor'