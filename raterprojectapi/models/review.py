from django.db import models
from django.db.models.deletion import CASCADE


class Review(models.Model):
    content = models.TextField()

    reviewer = models.ForeignKey(
        "Gamer",
        on_delete=CASCADE,
        related_name="reviews",
        related_query_name="review"
    )

    game = models.ForeignKey(
        "Game",
        on_delete=CASCADE,
        related_name="reviews",
        related_query_name="review"
    )
