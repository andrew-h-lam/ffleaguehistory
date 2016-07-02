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
    week_number =  models.IntegerField()
    playoff_round = models.IntegerField()
    home_team = models.ForeignKey(Player, related_name='home_team')
    home_team_score = models.IntegerField()
    away_team = models.ForeignKey(Player, related_name='away_team')
    away_team_score = models.IntegerField()

class Payout(models.Model):
    season = models.ForeignKey(Season)
    player = models.ForeignKey(Player)
    description = models.CharField(max_length=50)
    amount = models.IntegerField()
