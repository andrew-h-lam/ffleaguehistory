from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + self.last_name

class Season(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    buy_in = models.IntegerField()

    def __str__(self):
        return self.name

class Matchup(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    week_number =  models.IntegerField()
    home_team = models.ForeignKey(Player, on_delete=models.CASCADE)
    home_team_score = models.IntegerField()
    away_team = models.ForeignKey(Player, on_delete=models.CASCADE)
    away_team_score = models.IntegerField()

class Payout(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
