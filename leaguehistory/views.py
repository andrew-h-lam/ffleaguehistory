from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Season, Player, Matchup, Payout, Standings
from django.db.models import Sum


def index(request):
    all_season = Season.objects.all()
    all_player = Player.objects.order_by('first_name')
    context = {
        'all_season': all_season,
        'all_player': all_player
    }
    return render(request, 'index.html', context)

def player_index(request):
    context = {
    }
    return render(request, 'player.html', context)

def player_detail(request, player_id):

    try:
        player = Player.objects.get(id=player_id)
        standings = Standings.objects.select_related('season').filter(player_id=player_id)
        total_wins = Standings.objects.filter(player_id=player_id).aggregate(wins=Sum('wins'))
        total_losses = Standings.objects.filter(player_id=player_id).aggregate(losses=Sum('losses'))
        total_ties = Standings.objects.filter(player_id=player_id).aggregate(ties=Sum('ties'))

        context = {
            'player': player,
            'standings': standings,
            'total_wins': total_wins,
            'total_losses': total_losses,
            'total_ties': total_ties
        }
    except Player.DoesNotExist:
        raise Http404("Player does not exist")

    return render(request, 'player/player_detail.html', context)

def season_index(request):
    context = {

    }
    return render(request, 'season.html', context)

# HTTP request passed in
def season_detail(request, season_id):
    try:
        season = Season.objects.get(id=season_id)
    except Season.DoesNotExist:
        raise Http404("Season does not exist")

    players = Matchup.objects.order_by('home_team_id').values('home_team_id').distinct()
    payouts = Payout.objects.select_related('player').filter(season_id=season_id)
    standings = Standings.objects.select_related('player').filter(season_id=season_id)

    context = {
        'season': season,
        'players': players,
        'payouts': payouts,
        'standings': standings
    }

    return render(request, 'season/season_detail.html', context)
