from django.contrib import admin
from .models import Player, Season, Matchup, Payout

admin.site.register(Player)
admin.site.register(Season)
admin.site.register(Matchup)
admin.site.register(Payout)