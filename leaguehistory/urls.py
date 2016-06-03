from django.conf.urls import url
from . import views

urlpatterns = [
    # /leaguehistory/
    url(r'^$', views.index, name='index'),

    #/player
    url(r'^player$', views.player_index, name='player_index'),

    # /player/12/
    #url(r'^player/(?P<player_id>[0-9]+)/$', views.player_detail, name='player_detail'),

    #/season
    url(r'^season$', views.season_index, name='season_index'),

    # /season/12/
    #url(r'^season/(?P<season_id>[0-9]+)/$', views.season_detail, name='season_detail'),

]
