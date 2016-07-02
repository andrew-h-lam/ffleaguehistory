from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Season, Player, Matchup, Payout

def index(request):
    all_season = Season.objects.all()
    context = {
        'all_season': all_season,
    }
    return render(request, 'index.html', context)

def player_index(request):
    context = {
    }
    return render(request, 'player.html', context)

def season_index(request):
    context = {
    }
    return render(request, 'season.html', context)

# HTTP request passed in
def season_detail(request, season_id):
    try:
        season = Season.objects.get(id=season_id)
        context = {
            'season': season,
        }
    except Season.DoesNotExist:
        raise Http404("Season does not exist")

    return render(request, 'season/season_detail.html', context)