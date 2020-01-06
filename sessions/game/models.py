from django.db import models


class Player(models.Model):
    game = models.ManyToManyField('Game', through='PlayerGameInfo')

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class Game(models.Model):
    exist = models.BooleanField()
    count = models.IntegerField()

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class PlayerGameInfo(models.Model):

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    try_count = models.IntegerField(default=0)
    author = models.BooleanField()
    winner = models.BooleanField(null=True)
