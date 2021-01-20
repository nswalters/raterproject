from rest_framework.viewsets import ModelViewSet
from raterprojectapi.models import Game
from raterprojectapi.serializers import GameSerializer


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
