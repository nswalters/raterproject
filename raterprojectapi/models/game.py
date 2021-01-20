from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=150)
    designer = models.CharField(max_length=50)
    year_released = models.DateField()
    number_of_players = models.IntegerField()
    age_recommendation = models.IntegerField()
    time_to_play = models.IntegerField()
    image = models.ImageField()

    categories = models.ManyToManyField(
        "Category",
        related_name="category_games",
        related_query_name="category_game"
    )
