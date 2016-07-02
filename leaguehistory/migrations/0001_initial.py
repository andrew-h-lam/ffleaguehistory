# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-04 00:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matchup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_number', models.IntegerField()),
                ('home_team_score', models.IntegerField()),
                ('away_team_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('buy_in', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='payout',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaguehistory.Player'),
        ),
        migrations.AddField(
            model_name='payout',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaguehistory.Season'),
        ),
        migrations.AddField(
            model_name='matchup',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='leaguehistory.Player'),
        ),
        migrations.AddField(
            model_name='matchup',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='leaguehistory.Player'),
        ),
        migrations.AddField(
            model_name='matchup',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaguehistory.Season'),
        ),
    ]