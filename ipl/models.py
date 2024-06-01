from django.db import models
# Create your models here.


class MatchesEntry(models.Model):
    ID = models.IntegerField(primary_key=True)
    season = models.CharField(default='0000', max_length=4)
    city = models.CharField(default='Virtual', max_length=35)
    date = models.DateField()
    team1 = models.CharField(max_length=35)
    team2 = models.CharField(max_length=35) 
    toss_winner = models.CharField(max_length=35)
    toss_decision = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    dl_applied = models.BooleanField()
    winner = models.CharField(max_length=35)
    win_by_runs = models.IntegerField()
    win_by_wickets = models.IntegerField()
    player_of_match = models.CharField(max_length=35)
    venue = models.CharField(max_length=50)
    umpire1 = models.CharField(max_length=35)
    umpire2 = models.CharField(max_length=35)
    umpire3 = models.CharField(max_length=35)


class DeliveriesEntry(models.Model):
    match_id = models.ForeignKey(MatchesEntry, on_delete=models.CASCADE)
    inning = models.IntegerField()
    batting_team = models.CharField(max_length=100)
    bowling_team = models.CharField(max_length=100)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=100)
    non_striker = models.CharField(max_length=100)
    bowler = models.CharField(max_length=100)
    is_super_over = models.BooleanField()
    wide_runs = models.IntegerField(default=0)
    bye_runs = models.IntegerField(default=0)
    legbye_runs = models.IntegerField(default=0)
    noball_runs = models.IntegerField(default=0)
    penalty_runs = models.IntegerField(default=0)
    batsman_runs = models.IntegerField(default=0)
    extra_runs = models.IntegerField(default=0)
    total_runs = models.IntegerField(default=0)
    player_dismissed = models.CharField(max_length=100, blank=True, null=True)
    dismissal_kind = models.CharField(max_length=100, blank=True, null=True)
    fielder = models.CharField(max_length=100, blank=True, null=True)