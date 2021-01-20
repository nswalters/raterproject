from rest_framework import serializers
from raterprojectapi.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('title', 'description', 'designer', 'year_released', 'number_of_players',
                  'age_recommendation', 'time_to_play', 'image', 'categories')
        depth = 1
