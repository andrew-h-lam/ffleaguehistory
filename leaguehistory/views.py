from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Player, Season, Matchup, Payout

def index(request):
    return render(request, 'index.html', '')

def player_index(request):
    context = {
    }
    return render(request, 'player.html', context)

def season_index(request):
    context = {
    }
    return render(request, 'season.html', context)
