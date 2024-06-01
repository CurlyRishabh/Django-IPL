from django.shortcuts import render
from django.db.models import Sum, Count, F, FloatField, ExpressionWrapper
from ipl.models import MatchesEntry, DeliveriesEntry
from django.http import JsonResponse


# Create your views here.

# 1 Number of matches played per year for all the years in IPL.
def matches_played_per_year(request):
    result_data = MatchesEntry.objects.values('season')\
        .annotate(count=Count('season'))
    return JsonResponse({
        "datasets": list(result_data)
    })


# 2 Number of matches won per team per year in IPL.
def matches_won_per_team_per_year(request):
    result_data = MatchesEntry.objects.values('winner', 'season')\
        .annotate(count=Count('ID'))

    return JsonResponse({
        "datasets": list(result_data)
    })


# 3 Extra runs conceded per team in the year 2016
def extra_run_conceded_2016(request):
    matches_subquery = MatchesEntry.objects.filter(season='2016').values('ID')
    result_data = (
        DeliveriesEntry.objects
        .filter(match_id__in=matches_subquery)
        .values('bowling_team')
        .annotate(run_conceded=Sum('extra_runs'))
        .order_by('run_conceded')
    )

    return JsonResponse({
        "datasets": list(result_data)
    })


# 4 Top 10 economical bowlers in the year 2015
def top_10_economical_bowler_2015(request):
    subquery_matches = MatchesEntry.objects.filter(season='2016').values('ID')

    result_data = (
        DeliveriesEntry.objects.filter(match_id__in=subquery_matches)
        .values('bowler')
        .annotate(
            runs=Sum('total_runs'),
            balls=Count('id'),
            economy=ExpressionWrapper(
                F('runs') / (F('balls') / 6.0), output_field=FloatField()
            ),
        )
        .filter(balls__gt=36)
        .order_by('economy')[:10]
    )

    return JsonResponse({
        "datasets": list(result_data)
    })
