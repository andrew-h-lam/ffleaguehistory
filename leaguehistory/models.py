from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Season(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    sub_id = models.IntegerField()
    buy_in = models.IntegerField()

    def __str__(self):
        return self.name

class Matchup(models.Model):
    season = models.ForeignKey(Season)
    week =  models.IntegerField()
    playoff = models.IntegerField()
    manager = models.ForeignKey(Player, related_name='manager')
    score = models.IntegerField()
    opponent = models.ForeignKey(Player, related_name='opponent')
    opponent_score = models.IntegerField()
    result = models.CharField(max_length=4)
    at_home = models.BooleanField()

    def __str__(self):
         return self.player.first_name + " " + self.player.last_name + " vs. " + self.player.first_name + " " + self.player.last_name

class Payout(models.Model):
    season = models.ForeignKey(Season)
    player = models.ForeignKey(Player)
    description = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return self.season.name + " - " + self.description

class Record(models.Model):
    season = models.ForeignKey(Season)
    player = models.ForeignKey(Player)
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()

    def __str__(self):
        return self.season.name + " - " + self.player.first_name + " " + self.player.last_name

