from django.db import models
from django.db.models.deletion import CASCADE


class Rating(models.Model):
    rating = models.IntegerField()

    rater = models.ForeignKey(
        "Gamer",
        on_delete=CASCADE,
        related_name="ratings",
        related_query_name="rating"
    )

    game = models.ForeignKey(
        "Game",
        on_delete=CASCADE,
        related_name="ratings",
        related_query_name="rating"
    )
